# Handles processing of order information and displaying it to the user
from django.db import models
from .Item import Item
from .User import User
import datetime

class Order(models.Model):
    #create fields for an order in db
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    #method to place order, saves info to db as order
    def placeOrder(self):
        self.save()

    #method to retrieve information about all orders from a given user, ordered by date
    @staticmethod
    def get_orders_from_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')