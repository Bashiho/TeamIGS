# Handles User information and account management
# Placeholder, find best way to pull information from the database later once database is established
name = 'accountName'
password = 'accountPassword'
email = 'accountEmail'
phone = 'accountPhone'
address = 'accountAddress'

# This is a placeholder for the User class
class User:
    def __init__(self, name, password, email, phone, address):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address

    # View Account Page
    def accountPage(self):
        # Placeholder for account page method
        pass

    # Login to account
    def login(self):
        # Placeholder for login method
        pass

    # Logout of account
    def logout(self):
        # Placeholder for logout method
        pass
    
    # Register an Account
    def register(self):
        # Placeholder for register method
        # Should use an email and password to register
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
    def viewOrders(self):
        # Placeholder for view orders method
        pass
    # View Wishlist
    def viewWishlist(self):
        # Placeholder for view wishlist method
        pass

    # View Cart
    def viewCart(self):
        # Placeholder for view cart method
        pass
    