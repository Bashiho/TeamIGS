from django.contrib import admin
from .Item import Item, Product # change Product to whatever subclass is added to Item.py

# Allows for editing product information when creating page for a product
class ItemInLine(admin.TabularInline):
    model = Product # Change to whatever subclass is in Item.py, currently placeholder
    extra =  1 # of fields needed
    
class ItemAdmin(admin.ModelAdmin):
    fieldsets = [ # Fields of information that is needed from Item class
        (None, {"fields": ["name"]}),
        ("Product description", {"fields": ["description"]}),
        (None, {"fields": ["imageURL"]}),
        ("Price", {"fields": ["price"]}),
        ("Category", {"fields": ["category"]}),
    ]
    inlines = [ItemInLine] # Required for InformationInLine to be read when creating product page
    # Configures how information about each Item object is displayed on admin page
    list_display = ["name", "description", "imageURL", "price", "category"] # What information is displayed above list in order
    list_filter = ["name", "category", "price"] # What items are filtered by
    search_fields = ["name", "category"] # What fields can be searched for

admin.site.register(Item, ItemAdmin) # Registers this information to the database