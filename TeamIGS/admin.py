from django.contrib import admin
from .Item import Item

# Allows for editing product information when creating page for a product
class InformationInLine(admin.TabularInline):
    model = Item
    # Add more for what information would be needed when creating an Item
    # Unsure of exactly what it would entail, possible that 'extra = x' where x is the amount of fields might work

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [ # Fields of information that is needed from Item class
        (None, {"fields": ["name"]}),
        ("Product description", {"fields": ["description"]}),
        (None, {"fields": ["imageURL"]}),
        ("Price", {"fields": ["price"]}),
    ]
    inlines = [InformationInLine] # Required for InformationInLine to be read when creating product page
    # Configures how information about each Item object is displayed on admin page
    list_display = ["name", "description", "imageURL", "price"] # What information is displayed above list in order
    list_filter = ["name"] # What items are filtered by
    search_fields = ["name"] # What fields can be searched for

admin.site.register(Item, ItemAdmin)