# Handles information of items, such as their price and descriptions, and displaying them to users
# Might have to rename to models.py for django, unsure
from django.db import models
from django.contrib import admin

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # find way to include product image
    imageURL = models.CharField(max_length=200)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2) # using to test error when creating item
    category = models.CharField(max_length=100)
    
    def __str__(self):
        #might be able to change it to just return name, requires testing and research
        returnString = self.name + " " + self.description + " " +  self.imageURL + " " +  str(self.price) 
        return returnString
    # @admin.display( #can be used to modify admin display
            
    # )

# Placeholder class, used for data fields of an item, might not be used
class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


    