from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings


class Customer(models.Model):
    """Model stored in each instance alongside cart. Mostly used for accounts in the event that they are implemented.
    
    Code Date: March 30
    Programmer: Russell de Vries

    Variables:
    User (auth.User): Django's built in User class, used for handling signing in/out of an account.
    name (str): String containing account name.
    email (str): String containing user's email.
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    @classmethod
    def create(cls, user, name, email):
        customer = cls(user=user, name=name, email=email)
        return customer

    def __str__(self):
        """Returns customer's name as string"""
        return self.name


class Item(models.Model):
    """Model that defines the items to be sold on the Ecommerce site.
    
    Code Date: March 30
    Programmer: Russell de Vries

    Variables:
    name (str): String containing name of item.
    description (str): String containing a brief description of item.
    image (image): Contains path to image of an item.
    price (double): Double containing price of an item.
    Category (Category): Category of an item.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    class Meta:
        """Provides information about how this class should be seen in database"""
        ordering = ('name',)
    
    @classmethod
    def create(cls, name, description, image, price):
        item = cls(name=name, description=description, image=image, price=price)
        return item

    def __str__(self):
        """Returns Item name as a string"""
        return self.name


class Order(models.Model):
    """Model containing information about a user's order. Used alongside cart.

    Code Date: April 1
    Programmer: Russell de Vries
    
    Variables:
    Customer (Customer): Customer that an order is tied to.
    dateOrdered (): Time that an order was created.
    complete (boolean): If the order is completed or not.
    transactionId (str): Id of the transaction.
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transactionId = models.CharField(max_length=100, null=True)

    @classmethod
    def create(cls, customer, dateOrdered, complete, transactionId):
        order = cls(customer=customer, dateOrdered=dateOrdered, complete=complete, transactionId=transactionId)
        return order

    def __str__(self):
        """Returns order's id"""
        return str(self.id)

    @property
    def get_cart_total(self):
        """Returns total cost of all items in the cart"""
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        """Returns all items in cart"""
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    """Model that handles items within an order. Always used alongside :models:'Order'.
    
    Code Date: April 1
    Programmer: Russell de Vries
    
    Varaibles:
    User (auth.User): User that the order is tied to.
    quantity (int): Amount of the item that is in the cart.
    Item (Item): Item that is being referred to.
    ordered (boolean): Boolean on if the item has been ordered or not.
    Order (Order): Order that the OrderItem is tied to.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default = False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)


    @classmethod
    def create(cls, user, quantity, item, ordered, order):
        orderItem = cls(user=user,quantity=quantity,item=item, ordered=ordered, order=order)
        return orderItem
        
    def __str__(self):
        """Returns how many of an item is in the cart"""
        return f"{self.quantity} of {self.item.name}"

    def getTotalItemPrice(self):
        """Returns the total cost of an item in the cart based on quantity in cart."""
        return self.quantity * self.item.price



'''
class Category(models.Model):
    """Defines a cateogry for an item. Currently has no use, but could be used in the future to implement a sorting system.
    Related to Item.

    Variables:
    name (string): String that contains the name of the Category.
    """
    name = models.CharField(max_length=50)

    class Meta:
        """Provides information about how this class should be seen in database"""
        ordering = ('name',)
        verbose_name_plural = "Categories"

    # returns all categories
    @staticmethod
    def get_all_categories():
        """Returns a list of all categories"""
        return Category.objects.all()

    def __str__(self):
        """Returns category name as a string"""
        return self.name
'''