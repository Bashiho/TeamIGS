from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.views.generic import View, ListView, DetailView
# Needed for account implementation, not working on yet
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Category, Customer, Item, Order, OrderItem
from .utilities import cartFromCookie
import json
import datetime
from django.core.mail import send_mail

def index(request):
    items = Item.objects.order_by("name")
    context={'items':items}
    return render(request, 'TeamIGS/index.html', context)

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"

def cart(request):
    cartData = cartFromCookie(request)
    order = cartData['order']
    items = cartData['items']
    
    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/cart.html', context)
        
def updateItem(request):
	data = json.loads(request.body)
	itemId = data['itemId']
	action = data['action']

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

def checkout(request):
    cartData = cartFromCookie(request)
    cartItems = cartData['cartItems']
    order = cartData['order']
    items = cartData['items']

    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/checkout.html', context)

def processOrder(request):
    # Potentially set up a process to email the user with information about the order
    # send_mail(
    #     "TeamIGS Order",
    #     "Order Confirmation from TeamIGS" + items,
    #     "TeamIGS@business.net",
    #     email,
    #     fail_silently= False
    # )
    return render(request, 'TeamIGS/processOrder.html')
