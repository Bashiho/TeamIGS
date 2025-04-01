from django.contrib import admin
from .Item import Item
from .Category import Category

# Allows for editing product information when creating page for a product
# class ItemInLine(admin.TabularInline):
    # model = product
    
class ItemAdmin(admin.ModelAdmin):
    fieldsets = [ # Fields of information that is needed from Item class
        (None, {"fields": ["name"]}),
        ("Product description", {"fields": ["description"]}),
        (None, {"fields": ["image"]}),
        ("Price", {"fields": ["price"]}),
        ("Category", {"fields": ["category"]}),
    ]
    # inlines = [ItemInLine] # Required for InformationInLine to be read when creating product page
    # Configures how information about each Item object is displayed on admin page
    list_display = ["name", "description", "image", "price", "category"] # What information is displayed above list in order
    list_filter = ["name", "category"] # What items are filtered by
    search_fields = ["name", "category"] # What fields can be searched for

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]})
    ]

admin.site.register(Item,ItemAdmin) # Registers this information to the database
admin.site.register(Category, CategoryAdmin)