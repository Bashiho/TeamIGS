from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


    # returns all categories
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=200, db_index=True, default=1)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def getAbsoluteURL(self):
        return reverse("TeamIGS:detail", kwargs={'slug': self.slug})
    
    def getAddToCartURL(self):
        return reverse("TeamIGS:add-to-cart", kwargs={'slug', self.slug})

    def getRemoveFromCartURL(self):
        return reverse("TeamIGS:remove-from-cart", kwargs={'slug', self.slug})


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default = False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def getTotalItemPrice(self):
        return self.quantity * self.item.price
