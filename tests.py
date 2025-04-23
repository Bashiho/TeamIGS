import unittest
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'TeamIGS.settings'
django.setup()


from TeamIGS.models import Customer, Item, Order, OrderItem

class CustomerTestCase():
    def setup(self):
        self.customer = Customer.create(user, name, email)
    
    def testDefaultUser(self):
        assert customer.user == user, "incorrect default user"

    def testDefaultName(self):
        assert customer.name == name, "incorrect default name"
    
    def testDefaultEmail(self):    
        assert customer.email == email, "incorrect default email"

CustomerTestSuite = unittest.TestSuite()

class ItemTestCase():
    def setup(self):
        self.item = Item.create(name, description, image, price)

    def testDefaultName(self):
        assert item.name == name, "incorrect default name"
        
    def testDefaultDescription(self):
        assert item.description == description, "incorrect default description"
        
    def testDefaultImage(self):
        assert item.image == image, "incorrect default image"
        
    def testDefaultPrice(self):
        assert item.price == price, "incorrect default price"

ItemTestSuite = unittest.TestSuite()

class OrderTestCase():
    def setup(self):
        self.order = Order.create(customer, dateOrdered, complete, transactionId)

    def testDefaultCustomer(self):
        assert order.customer == customer, "incorrect default customer"

    def testDefaultDateOrdered(self):
        assert order.dateOrdered == dateOrdered, "incorrect default dateOrdered"

    def testDefaultComplete(self):
        assert order.complete == complete, "incorrect default complete"

    def testDefaultTransactionID(self):
        assert order.transactionId == transactionId, "incorrect default transactionId"

OrderTestSuite = unittest.TestSuite()

class OrderItemTestCase(unittest.TestCase):
    def runTest(self):
        # user = 
        quantity = 5
        # item = 
        ordered = True
        # order = 
        self.orderItem = OrderItem.create(user, quantity, item, ordered, order)

    def tearDown(self):
        self.orderItem.dispose()
        self.orderItem = None

    def testDefaultUser(self):
        assert orderItem.user == user, "incorrect default user"

    def testDefaultQuantity(self):
        assert orderItem.quantity == quantity, "incorrect default quantity"

    def testDefaultItem(self):
        assert orderItem.item == item, "incorrect default item"

    def testDefaultOrdered(self):
        assert orderItem.ordered == ordered, "incorrect default ordered"

    def testDefaultOrder(self):
        assert orderItem.order == order, "incorrect default order"

OrderItemTestSuite = unittest.TestSuite()
OrderItemTestSuite.addTest(OrderItemTestCase("testDefaultUser"))
OrderItemTestSuite.addTest(OrderItemTestCase("testDefaultQuantity"))
OrderItemTestSuite.addTest(OrderItemTestCase("testDefaultItem"))
OrderItemTestSuite.addTest(OrderItemTestCase("testDefaultOrdered"))
OrderItemTestSuite.addTest(OrderItemTestCase("testDefaultOrder"))
runner = unittest.TextTestRunner()
runner.run(OrderItemTestSuite)