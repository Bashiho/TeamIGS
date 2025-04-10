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
from .models import Category, Customer, Item, Order, OrderItem
import json
from .utilities import cartFromCookie

class IndexView(generic.ListView):
    template_name = "TeamIGS/index.html"
    context_object_name = "item_list"
    

    def get_queryset(self):
        return Item.objects.filter().order_by("name")

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"

def checkout(request):
    # Commented out until accounts are implemented to prevent bugs
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    cartData = cartFromCookie(request)
    cartItems = cartData['cartItems']
    order = cartData['order']
    items = cartData['items']

    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/checkout.html', context)

def cart(request):
    # Removing Temporarily until accounts are implemented
    # Causes errors when signed in to admin account and adding to/removing from cart
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    cartData = cartFromCookie(request)
    cartItems = cartData['cartItems']
    order = cartData['order']
    items = cartData['items']

    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'TeamIGS/cart.html/', context)
        

def updateItem(request):
	data = json.loads(request.body)
	itemId = data['itemId']
	action = data['action']
	print('Action:', action)
	print('Product:', itemId)

	customer = request.user.customer
	item = Product.objects.get(id=itemId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=item)

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

# class InCategoryView(generic.ListView):
#     template_name = "TeamIGS/InCategory.html"
#     context_object_name = "category_items"

#     def get_queryset(self):
#         categoryID = self.request.GET.get('category')
#         if categoryID:
#             return Item.objects.filter(category__name=categoryID)
#         else:  
#             return

# # Hasn't been tested
# # Might want to add email verification in the future, though that might be handled elsewhere
# def createAccount(request):
#     username = request.POST["username"]
#     email = request.POST["email"]
#     password = request.POST["password"]
#     firstName = request.POST["firstname"]
#     lastName = request.POST["lastname"]
#     user = User.objects.create_user(username, email, password)
#     user.first_name = firstName
#     user.last_name = lastName
#     messages.add_message(self.request, "Account Created!")
#     return render(self.request, 'TeamIGS/')

# # Directed to this page when attempting to sign in
# # Verifies account and sends to home or returns error and sends back to login page
# class loginView(generic.View):
#     template_name = "TeamIGS/login.html"

#     def loginView(request):
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username, password)
#         if user is not None:
#             login(request, user)
#             # Can make success page for login, otherwise this works
#             messages.add_message(self.request, "Successful login")
#             return render(self.request, 'TeamIGS/index.html')
#         else:
#             # Make failure page
#             messages.error(self.request, 'Failed to login')
#             return render(self.request, 'TeamIGS/login.html')