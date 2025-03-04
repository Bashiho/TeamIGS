# Not sure which ones will be used, can clean up later
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .Item import Item

class IndexView(generic.ListView):
    template_name = "TeamIGS/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        return Item.objects.filter().order_by("name")

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"

# View for cart, placeholder for now
class CartView(generic.DetailView):
    template_name = "TeamIGS/cart.html" #currently doesn't exist, create later

# placeholder method for adding items to cart, might be moved later
def add_to_cart():
    pass