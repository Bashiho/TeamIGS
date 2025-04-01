# Not sure which ones will be used, can clean up later
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .Item import Item
from .Order import Order
from .Category import Category
from .OrderItem import OrderItem

class IndexView(generic.ListView):
    template_name = "TeamIGS/index.html"
    context_object_name = "item_list"
    

    def get_queryset(self):
        return Item.objects.filter().order_by("name")

class DetailView(generic.DetailView):
    model = Item
    template_name = "TeamIGS/detail.html"


# # Requires updated implementation
# class CartView(generic.ListView):
#     template_name = "TeamIGS/cart.html"
#     context_object_name = "cart_items"

#     def get_queryset(self):
#         return Item.objects.filter() # Doesn't filter, fix later when rest is working

# Requires more implementation, currently always kicks user back to index but should visit page when
# user has items in cart
class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'TeamIGS/cart.html', context)
        except ObjectDoesNotExist:
            # messages.error(self.request, "There is no active order")
            return redirect("/")
            
# Category searching moved to low priority, return to this later
# class CategoryView(generic.ListView):
#     template_name = "TeamIGS/category.html"
#     context_object_name = "categories"

#     def get_queryset(self):
#         return Category.objects.order_by("name")

class InCategoryView(generic.ListView):
    template_name = "TeamIGS/InCategory.html"
    context_object_name = "category_items"

    def get_queryset(self):
        categoryID = self.request.GET.get('category')
        if categoryID:
            return Item.objects.filter(category__name=categoryID)
        else:  
            return