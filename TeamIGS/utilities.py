import json 
from .models import *

# Handles data of cart from cookie in views
def cartFromCookie(request):
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
        