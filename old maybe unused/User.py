# Handles User information and account management
# Placeholder, find best way to pull information from the database later once database is established
name = 'accountName'
password = 'accountPassword'
email = 'accountEmail'
phone = 'accountPhone'
address = 'accountAddress'
accountID = 'accountID'

# This is a placeholder for the User class
class User:
    def __init__(self, name, password, email, phone, address, accountID):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
        self.accountID = accountID

    # View Account Page
    def accountPage(self, accountID):
        # Placeholder for account page method
        pass

    # Login to account
    def login(self, email, password):
        # Placeholder for login method
        # Ensure that there is some way for page to know if login attempt was successful
        # Check for corrent information
        pass

    # Logout of account
    def logout(self):
        # Placeholder for logout method
        # Ensure that page knows if logout attempt was successful
        pass
    
    # Register an Account
    def register(self, email, password):
        # Placeholder for register method
        # Should use an email and password to register
        # Could verify account upon creation using email, unnecessary but could be useful addition
        pass

    # Update Account Information
    def updateProfile(self):
        # Placeholder for update profile method
        # Determine best security method
            # Options are - Security Question, Email Verification, SMS Verification
        pass

    # Update Password 
    def resetPassword(self):
        # Placeholder for reset password method
        # Determine best security method
            # Options are - Security Question, Email Verification, SMS Verification
        pass

    # View Orders
    def viewOrders(self, accountID):
        # Placeholder for view orders method
        # Could associate accountID with orders in database to allow for filtering
        pass

    # View Wishlist
    def viewWishlist(self, accountID):
        # Placeholder for view wishlist method
        pass

    # View Cart
    def viewCart(self):
        # Placeholder for view cart method
        pass
    