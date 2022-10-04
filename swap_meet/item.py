
class Item:
    def __init__(self, category = ""):
        self.category = category
    
"""
Instances of Vendor have an instance method named get_by_category

It takes one argument: a string, representing a category
This method returns a list of Items in the inventory with that category
"""
