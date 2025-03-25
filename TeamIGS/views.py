# Not sure which ones will be used, can clean up later
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .Item import Item
from .Cart import Cart
from .Category import Category

class IndexView(generic.ListView):
    template_name = "TeamIGS/index.html"
    context_object_name = "item_list"
    

    def get_queryset(self):
        return Item.objects.filter().order_by("name")

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"

class CartView(generic.ListView):
    model = Cart
    template_name = "TeamIGS/cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return Cart.objects.order_by("item") # Might be handled in Cart.py, requires research

class CategoryView(generic.ListView):
    template_name = "TeamIGS/category.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.order_by("name")
    
class InCategoryView(generic.ListView):
    template_name = "TeamIGS/inCategory.html"
    context_object_name = "category_items"

    def get_queryset(self):
        return Item.objects.filter(category=Category).order_by("name")
    