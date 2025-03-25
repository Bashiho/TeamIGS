# Handles information of items, such as their price and descriptions, and displaying them to users
from django.db import models
from django.contrib import admin
from .Category import Category

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='templates/uploads/products/', default=1) # Allows admin to upload image for product when creating product
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    # Shows Items by name instead of ID when working in DB
    def __str__(self):
        return self.name


# Placeholder class, might not be used
class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


    