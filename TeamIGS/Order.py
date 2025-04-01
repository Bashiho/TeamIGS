# Handles processing of order information and displaying it to the user
# Might serve same function as cart, requires more development to be sure
from django.db import models
from .Item import Item
from .User import User
from .OrderItem import OrderItem
import datetime
from django.conf import settings

class Order(models.Model):
    #create fields for an order in db
    items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    #method to place order, saves info to db as order
    def __str__(self):
        return self.user.username

    def getTotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.getTotalItemPrice()
        return total

    # might be removed later or placed elsewhere, currently placeholder
    # method to retrieve information about all orders from a given user, ordered by date
    @staticmethod
    def get_orders_from_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')