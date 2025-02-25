# Handles information of items, such as their price and descriptions, and displaying them to users
# Might have to rename to models.py for django, unsure
from django.db import models
from django.contrib import admin

class Item(models.Model):
    #sets max size for attribute fields for products
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # find way to include product image
    imageURL = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    
    def __str__(self):
        return self.name, self.description, self.imageURL, self.price
    # @admin.display( #can be used to modify admin display
            
    # )

class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    