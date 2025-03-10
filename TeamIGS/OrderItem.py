# Handles ordering of items
from .Item import Item
from .Cart import Cart
from .Payment import Payment
from .User import User
from .Shipping import Shipping

class OrderItems():
    # currency = find appropriate currency and apply
    userID = User.getID() # gets user's ID
    cart = getCart(userID) # retrieves user's cart
    total = Payment.getTotal(cart) # calls method in Payment to final total including shipping and taxes
    Payment.takePayment(total) # Calls TakePayment() in .Payment to handle payment w/ given information
    placeOrder() # placeholder


    def placeOrder():
        return