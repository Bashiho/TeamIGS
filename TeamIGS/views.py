# Not sure which ones will be used, can clean up later
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .Item import Item

# View containing all items available on site, mostly placeholder for now
class IndexView(generic.ListView):
    template_name = "teamIGS/index.html" #currently doesn't exist, create later

# View containing detailed item page, mostly placeholder for now
class DetailView(generic.DetailView):
    model = Item
    template_name = "teamIGS/detail.html" #currently doesn't exist, create later

# View for cart, placeholder for now
class CartView(generic.DetailView):
    template_name = "teamIGS/cart.html" #currently doesn't exist, create later

# placeholder method for adding items to cart, might be moved later
def add_to_cart():
    pass