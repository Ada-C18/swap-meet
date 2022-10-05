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

    def swap_best_by_category(self, other, my_priority, their_priority):
        """ 
        - `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
  - It takes in three arguments
    - `other`, which represents another `Vendor` instance to trade with
    - `my_priority`, which represents a category that the `Vendor` wants to receive
    - `their_priority`, which represents a category that `other` wants to receive
  - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
    - It returns `True`
    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
        """

        my_item_to_give = self.get_best_by_category(category=their_priority)
        their_item_to_give = other.get_best_by_category(category=my_priority)
        if my_item_to_give == None or their_item_to_give == None:
            return False 
        self.swap_items(other, my_item_to_give, their_item_to_give)
        return True 


