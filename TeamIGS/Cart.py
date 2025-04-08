# handles Cart objects that contain items for customer orders
from django.db import models
from .Item import Item
from .Customer import Customer

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


    # method to be called when viewing cart
    def viewCart(self):
        return Cart.objects.order_by("item")

    # placeholder
    def getTotal(self):
        total = 0
        for items in Cart:
            total += item.price
        return total