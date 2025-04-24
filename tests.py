from django.test import TestCase
from decimal import *
import datetime
from django.contrib.auth.models import User
from TeamIGS.models import Customer, Item, Order, OrderItem

class ItemTestCase(TestCase):
    def setUp(self):
        image = 'TeamIGS/static/images/itemImages/apple_crab.png' # Replace with whatever image you want to use for testing
        Item.objects.create(name="Lamp", description="Simple Lamp", image=image, price=71322.72)
        Item.objects.create(name="Chair", description="Simple Chair", image=image, price=52.16)

    def testItemName(self):
        lamp = Item.objects.get(name="Lamp")
        chair = Item.objects.get(name="Chair")
        self.assertEqual(lamp.name, "Lamp")
        self.assertEqual(chair.name, "Chair")

    def testItemDescription(self):
        lamp = Item.objects.get(name="Lamp")
        chair = Item.objects.get(name="Chair")
        self.assertEqual(lamp.description, "Simple Lamp")
        self.assertEqual(chair.description, "Simple Chair")

    def testItemImage(self):
        lamp = Item.objects.get(name="Lamp")
        chair = Item.objects.get(name="Chair")
        self.assertEqual(lamp.image, 'TeamIGS/static/images/itemImages/apple_crab.png')
        self.assertEqual(chair.image, 'TeamIGS/static/images/itemImages/apple_crab.png')

    def testItemPrice(self):
        lampPrice = 71322.72
        chairPrice = 52.16
        finalLampPrice = Decimal(str(lampPrice)).quantize(Decimal('.01'))
        finalChairPrice = Decimal(str(chairPrice)).quantize(Decimal('.01'))
        lamp = Item.objects.get(name="Lamp")
        chair = Item.objects.get(name="Chair")
        self.assertEqual(lamp.price, finalLampPrice)
        self.assertEqual(chair.price, finalChairPrice)

class CustomerTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="username", password="password", email="email@gmail.com")
        Customer.objects.create(user=user, name="Bob", email="email@gmail.com")
        Customer.objects.create(user=user, name="Gerald", email="email2@gmail.com")

    def testCustomerUser(self):
        user = User.objects.create(username="username", password="password", email="email@gmail.com")
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEquals(bob.user, user)
        self.asserEquals(gerald.user, user)

    def testCustomerName(self):
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEquals(bob.name, "Bob")
        self.asserEquals(gerald.name, "Gerald")

    def testCustomerEmail(self):
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEquals(bob.email, "email@gmail.com")
        self.asserEquals(gerald.email, "email2@gmail.com")

class OrderTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(user=user, name="Bob", email="email@gmail.com")
        Order.objects.create(customer=customer, dateOrdered=datetime.datetime(2025, 4, 24), complete=True, transactionId="abcdefghijklmnopqrstuvwxyz")
        Order.objects.create(customer=customer, dateOrdered=datetime.datetime(2025, 1, 9), complete=False, transactionId="123")

    def TestOrderCustomer(self):
        customer = Customer.objects.get(name="Bob")
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEquals(order1.customer, customer)
        self.assertEquals(order2.customer, customer)

    def TestOrderDateOrdered(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEquals(order1.dateOrdered, datetime.datetime(2025, 4, 24))
        self.assertEquals(order2.dateOrdered, datetime.datetime(2025, 1, 9))

    def TestOrderComplete(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEquals(order1.complete, True)
        self.assertEquals(order2.complete, False)

    def TestOrderTransactionID(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.asserEquals(order1.transactionId, "abcdefghijklmnopqrstuvwxyz")
        self.assertEquals(order2.transactionId, "123")

class OrderItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create() # Not sure how to get this working tbh
        lamp = Item.objects.get(name="Lamp")
        order = Order.objects.get(complete=True)
        OrderItem.objects.create(user=user, quantity=5, item=lamp, ordered=False, order=order)
        
    # def TestOrderItemUser(self):
        
    def TestOrderItemQuantity(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEquals(lamp.quantity, 5)

    # def TestOrderItemItem(self):
        
    def TestOrderItemOrdered(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEquals(lamp.ordered, False)

    def TestOrderItemOrder(self):
        order = Order.objects.get(complete=True)
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEquals(lamp.order, order)