# Handles information of items, such as their price and descriptions, and displaying them to users
from django.db import models
from django.contrib import admin
from .Category import Category

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True) # Need to fix upload location, html doesn't retrieve images properly
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=200, db_index=True, default=1)

    class Meta:
        ordering = ('name',)
        # index_together = (('id', 'slug'),) seems to cause errors, not sure why
    
    # Shows Items by name instead of ID when working in DB
    def __str__(self):
        return self.name

    def getAbsoluteURL(self):
        return reverse("TeamIGS:detail", kwargs={'slug': self.slug})
    
    # Requires adding something to urls.py
    def getAddToCartURL(self):
        return reverse("TeamIGS:add-to-cart", kwargs={'slug', self.slug})

    def getRemoveFromCartURL(self):
        return reverse("TeamIGS:remove-from-cart", kwargs={'slug', self.slug})

# # Placeholder class, might not be used
# class Product(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.category


    