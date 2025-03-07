# Handles information of items, such as their price and descriptions, and displaying them to users
from django.db import models
from django.contrib import admin

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # find way to include product image, might not use URL here
    imageURL = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    
    # used when looking at objects in database, represents them via their name
    def __str__(self):
        return self.name

    # @admin.display( #can be used to modify admin display

    # )

# Placeholder class, used for data fields of an item, might not be used
class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


    