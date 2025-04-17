from django.contrib import admin
from .models import Category, Customer, Item, Order
    
class ItemAdmin(admin.ModelAdmin):
    """Contains information about Items that is used on the admin page"""
    fieldsets = [ # Fields of information that is needed from Item class
        (None, {"fields": ["name"]}),
        ("Product description", {"fields": ["description"]}),
        (None, {"fields": ["image"]}),
        ("Price", {"fields": ["price"]}),
        ("Category", {"fields": ["category"]}),
    ]
    # Configures how information about each Item object is displayed on admin page
    list_display = ["name", "description", "image", "price", "category"] # What information is displayed above list in order
    list_filter = ["name", "category"] # What items are filtered by
    search_fields = ["name", "category"] # What fields can be searched for

class CategoryAdmin(admin.ModelAdmin):
    """Contains information about Categories to be used on the admin page"""
    fieldsets = [
        (None, {"fields": ["name"]})
    ]

# Registers these models on the admin site
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Item,ItemAdmin)
admin.site.register(Category, CategoryAdmin)