# Handles payments
from .Shipping import Shipping
from .User import User
from .Cart import Cart
from .Item import Item

class Payment():
    # find way to get tax rate based on location of user
    # tax_rate = 
    def getTotal(cart):
        total = 0 # initializes to 0
        for item in cart: # finds subtotal
            total += item.price
        # check order in which these are calculated to be sure
        total = subTotal + Shipping.getCost() # adds shipping
        total = total * tax_rate # handles taxes
        return total

    # placeholder method, implement later
    def takePayment(total):
        return

