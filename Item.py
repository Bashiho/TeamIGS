# Handles information of items, such as their price and descriptions, and displaying them to users
class Item():
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description