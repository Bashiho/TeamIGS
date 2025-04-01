# Handles management of items in cart
from .Item import Item
from .Cart import Cart
from .Payment import Payment
from .User import User
from .Shipping import Shipping
from django.db import models
from django.conf import settings

class OrderItem(models.Model):
    # currency = find appropriate currency and apply
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def getTotalItemPrice(self):
        return self.quantity * self.item.price
