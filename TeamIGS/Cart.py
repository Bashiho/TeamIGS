# handles Cart objects that contain items for customer orders
from django.db import models
from .Item import Item
from .User import User

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


    # method to be called when viewing cart
    def viewCart(self):
        return Cart.objects.order_by("item")
