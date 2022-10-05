from .item import Item

class Vendor:
    
    def __init__(self, inventory=None):
        """
        Set up a Vendor instance using an optional list of 
        inventory items. 
        """

        # set up default empty list for self.inventory
        # Conditional expression doc: 
        # https://docs.python.org/3/reference/expressions.html#conditional-expressions        
        self.inventory = inventory if inventory else []

    def add(self, item):
        """
        Add an item to self.inventory. Returns the item. 
        """

        self.inventory.append(item)
        return item 

    def remove(self, item):
        """
        Remove item from self.inventory. Returns the item if successful,
        returns False if item not found in self.inventory.
        """

        # Use try/except to catch error and return false if 
        # item is not in list. 
        try:
            self.inventory.remove(item)
            return item 
        except ValueError:
            return False 
    
    def get_by_category(self, category):
        """
        Returns a list of items in the inventory wihh the specified category
        """
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in other_vendor.inventory:
            return False
        
        self.add(their_item)
        self.remove(my_item)

        other_vendor.add(my_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_item, their_item)

        return True
    
    def get_best_by_category(self, category):
        """
        Takes a string category and returns the item with the 
        best condition matching the category.
        """

        category_list = [item for item in self.inventory if item.category == category]
        return max(category_list, default=None, key=lambda i:i.condition)

    def swap_best_by_category(other, my_priority=, their_priority="Decor"):
        pass 