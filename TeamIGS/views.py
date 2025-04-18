import django
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.views.generic import View, ListView, DetailView
# Needed for account implementation, not working on yet
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Customer, Item, Order, OrderItem
from .utilities import cartFromCookie
import json
import datetime
from django.core.mail import send_mail

def index(request):
    """Renders /templates/TeamIGS/index.html with list of all items sorted by name
    
    Code Date: April 15
    Programmer: Russell de Vries

    Code Date: April 10th
    Programmer: Finn Bishop
    
    Code Date: April 3
    Programmer: Andy Martinez
    """
    items = Item.objects.order_by("name")
    context={'items':items}
    return render(request, 'TeamIGS/index.html', context)

class DetailView(generic.DetailView):
    
    """Uses /TeamIGS/detail.html template to create page with description of a specific item
    
    Code Date: March 4
    Programmer: Russell de Vries
    
    Code Date: April 3
    Programmer: Andy Martinez
    """
    model = Item
    template_name = "TeamIGS/detail.html"

def cart(request):
    """Uses Cookies to retrieve cart object for user and renders the cart.html template using the cart
    
    Code Date: April 8
    Programmer: Russell de Vries

    Code Date: April 15th
    Programmer: Finn Bishop
    """
    cartData = cartFromCookie(request)
    order = cartData['order']
    items = cartData['items']
    
    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/cart.html', context)
        
def updateItem(request):
    """Used to update quantity of an item stored in the cart. Accessed from cart.html.

    Code Date: April 8
    Programmer: Russell de Vries
    
    Code Date: April 3
    Programmer: Andy Martinez
    
    Parameters:
    itemId (int): ID of the item that will be adjusted.
    action (str): Determines what will be done to the quantity, either adding to or removing from it.
    customer (customer): Customer object based on user given by cookie.
    item (item): Item determined by itemId.
    order (order): Order containing all items in cart.
    created (boolean): If the order had to be created or not.
    orderItem (orderItem): Item within the order.

    Returns: 
    jsonResponse: lets user know that the item was added/removed.
    """
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

    if action == 'add':
        return JsonResponse('Item was added', safe=False)
    else: 
        return JsonResponse('Item was removed', safe=False)

def checkout(request):
    """Renders checkout.html with list of items in cart given by cookie

    Code Date: April 15
    Programmer: Russell de Vries
    
    Code Date: April 1th
    Programmer: Finn Bishop
    Notes: Primary focus is on cart.html

    Code Date: April 3
    Programmer: Andy Martinez
    
    Parameters:
    cartData (dict): dictionary of all information in the user's cart
    order (order): Order object based on user's cart
    items (dict): Dictionary of items in cart

    Returns:
    Renders request with information about user's cart
    """
    
    cartData = cartFromCookie(request)
    order = cartData['order']
    items = cartData['items']

    context = {'items':items, 'order':order}
    return render(request, 'TeamIGS/checkout.html', context)

def processOrder(request):
    """Directs user to basic page reading "Order Complete", doesn't currently actually handle orders
    
    Code Date: April 15
    Programmer: Russell de Vries
    
    Code Date: April 3
    Programmer: Andy Martinez
    """
    # Potentially set up a process to email the user with information about the order
    # send_mail(
    #     "TeamIGS Order",
    #     "Order Confirmation from TeamIGS" + items,
    #     "TeamIGS@business.net",
    #     email,
    #     fail_silently= False
    # )
    return render(request, 'TeamIGS/processOrder.html')
