import json 
from .models import *

# Handles data of cart from cookie in views
def cartFromCookie(request):
    """Creates a cart dictionary from the cart cookie
    
    Variables: 
    cart (dict) = cart that is pulled from the cookie.
    items (arr) = Array of items in the cart.
    order (Order) = Order object with information from the cart.
    cartItems (int) = Number of items in cart

    Returns: Context with information about items, order, and cartItems
    """
    cart = json.loads(request.COOKIES['cart'])
    print("Cart:", cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']
    
    for i in cart:
        try:
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
        
        except:
            pass

    return {'cartItems':cartItems, 'order':order, 'items':items}
        