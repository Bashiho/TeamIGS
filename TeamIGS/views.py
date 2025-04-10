# Not sure which ones will be used, can clean up later
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .Item import Item
from .Order import Order
from .Category import Category
from .OrderItem import OrderItem
from .Customer import Customer
import json

class IndexView(generic.ListView):
    template_name = "TeamIGS/index.html"
    context_object_name = "item_list"
    

    def get_queryset(self):
        return Item.objects.filter().order_by("name")

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"


# # Requires updated implementation
# class CartView(generic.ListView):
#     template_name = "TeamIGS/cart.html"
#     context_object_name = "cart_items"

#     def get_queryset(self):
#         return Item.objects.filter() # Doesn't filter, fix later when rest is working

# Requires more implementation, currently always kicks user back to index but should visit page when
# user has items in cart
# class CartView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Order.objects.get(user=self.request.user, ordered=False)
#             context = {'object': order}
#             return render(self.request, 'TeamIGS/cart.html', context)
#         except ObjectDoesNotExist:
#             # messages.error(self.request, "There is no active order")
#             return redirect("/")

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'TeamIGS/checkout.html', context)

def cart(request):
    # if request.user.is_authenticated:
        # customer = request.user.customer
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
    # items = order.orderitem_set.all()
    # ese:
    cart = json.loads(request.COOKIES['cart'])
    print("Cart:", cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']
    
    for i in cart:
        cartItems += cart[i]['quantity']
        item = Item.objects.get(id=i)
        total = (item.price * cart[i]['quantity'])
        
        order['get_cart_total'] += total
        order['get_cart_items'] += cart[i]['quantity']

        item = {
            'item':{
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'image': item.image,
            },
            'quantity': cart[i]['quantity'],
            'get_total':total,
        }
        items.append(item)

    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/cart.html/', context)

def updateItem(request):
	data = json.loads(request.body)
	itemId = data['itemId']
	action = data['action']
	print('Action:', action)
	print('Item:', itemId)

	customer = request.user.customer
	item = Item.objects.get(id=itemId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
            
# Category searching moved to low priority, return to this later
# class CategoryView(generic.ListView):
#     template_name = "TeamIGS/category.html"
#     context_object_name = "categories"

#     def get_queryset(self):
#         return Category.objects.order_by("name")

class InCategoryView(generic.ListView):
    template_name = "TeamIGS/InCategory.html"
    context_object_name = "category_items"

    def get_queryset(self):
        categoryID = self.request.GET.get('category')
        if categoryID:
            return Item.objects.filter(category__name=categoryID)
        else:  
            return

# Hasn't been tested
# Might want to add email verification in the future, though that might be handled elsewhere
def createAccount(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    firstName = request.POST["firstname"]
    lastName = request.POST["lastname"]
    user = User.objects.create_user(username, email, password)
    user.first_name = firstName
    user.last_name = lastName
    messages.add_message(self.request, "Account Created!")
    return render(self.request, 'TeamIGS/')

# Directed to this page when attempting to sign in
# Verifies account and sends to home or returns error and sends back to login page
class loginView(generic.View):
    template_name = "TeamIGS/login.html"

    def loginView(request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            # Can make success page for login, otherwise this works
            messages.add_message(self.request, "Successful login")
            return render(self.request, 'TeamIGS/index.html')
        else:
            # Make failure page
            messages.error(self.request, 'Failed to login')
            return render(self.request, 'TeamIGS/login.html')