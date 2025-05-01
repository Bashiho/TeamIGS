from django.test import TestCase
from decimal import *
import datetime
from django.contrib.auth.models import User
from TeamIGS.models import Customer, Item, Order, OrderItem
from freezegun import freeze_time

class ItemTestCase(TestCase):
    def setUp(self):
        image = 'TeamIGS/static/images/cart-icon.png' # Replace with whatever image you want to use for testing
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
        self.assertEqual(lamp.image, 'TeamIGS/static/images/cart-icon.png')
        self.assertEqual(chair.image, 'TeamIGS/static/images/cart-icon.png')

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
        user = User.objects.create_user(username="username", password="password", email="email@gmail.com")
        user2 = User.objects.create_user(username="username2", password="password2", email="email2@gmail.com")
        Customer.objects.create(user=user, name="Bob", email="email@gmail.com")
        Customer.objects.create(user=user2, name="Gerald", email="email2@gmail.com")

    def testCustomerUser(self):
        user = User.objects.get(username="username")
        user2 = User.objects.get(username="username2")
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEqual(bob.user, user)
        self.assertEqual(gerald.user, user2)

    def testCustomerName(self):
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(gerald.name, "Gerald")

    def testCustomerEmail(self):
        bob = Customer.objects.get(name="Bob")
        gerald = Customer.objects.get(name="Gerald")
        self.assertEqual(bob.email, "email@gmail.com")
        self.assertEqual(gerald.email, "email2@gmail.com")

class OrderTestCase(TestCase):
    @freeze_time("2025-4-24")
    def setUp(self):
        image = 'TeamIGS/static/images/cart-icon.png'
        user = User.objects.create_user(username="username", password="password", email="email@gmail.com")
        user2 = User.objects.create_user(username="username2", password="password2", email="email2@gmail.com")
        customer = Customer.objects.create(user=user, name="Bob", email="email@gmail.com")
        customer2 = Customer.objects.create(user=user2, name="Gerald", email="email2@gmail.com")
        Order.objects.create(customer=customer, dateOrdered=datetime.datetime(2025, 4, 24, 0, 0, 0, tzinfo=datetime.timezone.utc), complete=True, transactionId="abcdefghijklmnopqrstuvwxyz")
        Order.objects.create(customer=customer2, dateOrdered=datetime.datetime(2025, 1, 9, 0, 0, 0, tzinfo=datetime.timezone.utc), complete=False, transactionId="123")
        order = Order.objects.get(customer=customer)
        Item.objects.create(name="Lamp", description="Simple Lamp", image=image, price=100)
        OrderItem.objects.create(user=user, quantity=5, item=Item.objects.get(name="Lamp"), ordered=False, order=order)

    def testOrderCustomer(self):
        customer = Customer.objects.get(name="Bob")
        customer2 = Customer.objects.get(name="Gerald")
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEqual(order1.customer, customer)
        self.assertEqual(order2.customer, customer2)

    @freeze_time("2025-4-28")
    def testOrderDateOrdered(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEqual(order1.dateOrdered, datetime.datetime(2025, 4, 24, 0, 0, 0, tzinfo=datetime.timezone.utc))
        
    def testOrderComplete(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEqual(order1.complete, True)
        self.assertEqual(order2.complete, False)

    def testOrderTransactionID(self):
        order1 = Order.objects.get(complete=True)
        order2 = Order.objects.get(complete=False)
        self.assertEqual(order1.transactionId, "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(order2.transactionId, "123")

    # def testGetCartTotal(self):
    #     order = Order.objects.get(complete=True)
    #     orderItem = OrderItem.objects.get(ordered=False)
    #     self.assertEqual(order.getCartTotal(), OrderItem.getTotalItemPrice())

class OrderItemTestCase(TestCase):
    def setUp(self):
        image = 'TeamIGS/static/images/cart-icon.png'
        Item.objects.create(name="Lamp", description="Simple Lamp", image=image, price=100)
        lamp = Item.objects.get(name="Lamp")

        user = User.objects.create_user(username="username", password="password", email="email@gmail.com")
        
        customer = Customer.objects.create(user=user, name="Bob", email="email@gmail.com")
        Order.objects.create(customer=customer, dateOrdered=datetime.datetime(2025, 4, 24), complete=True, transactionId="abcdefghijklmnopqrstuvwxyz")
        order = Order.objects.get(complete=True)

        OrderItem.objects.create(user=user, quantity=5, item=Item.objects.get(name="Lamp"), ordered=False, order=order)
        
    def testOrderItemUser(self):
        user = User.objects.get(username="username")
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEqual(lamp.user, user)
        
    def testOrderItemQuantity(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEqual(lamp.quantity, 5)

    def testOrderItemItem(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        lampItem = Item.objects.get(name="Lamp")
        self.assertEqual(lamp.item, lampItem)
        
    def testOrderItemOrdered(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEqual(lamp.ordered, False)

    def testOrderItemOrder(self):
        order = Order.objects.get(complete=True)
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEqual(lamp.order, order)

    def testGetTotalItemPrice(self):
        lamp = OrderItem.objects.get(item=Item.objects.get(name="Lamp"))
        self.assertEqual(lamp.getTotalItemPrice(), 500)