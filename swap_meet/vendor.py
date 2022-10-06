from queue import PriorityQueue
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory  = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            item not in self.inventory
            return False
    
    def get_by_category(self,category):
        category_list= []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
    
    def swap_items(self, other_vendor, my_item,their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            other_vendor.add(my_item)
            self.inventory.append(their_item)
            other_vendor.remove(their_item)
            return True
        
#Wave 4
    def swap_first_item(self, other_vendor):
        if len(self.inventory) < 1 or len(other_vendor.inventory) < 1:
            return False
        else:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_best_by_category(self, category):
        best_list = self.get_by_category(category)
        best_item = ""
        best_rating = 0
        if len(best_list) < 1:
            return None
        for item in best_list:
            if item.condition > best_rating:
                best_item = item
                best_rating = item.condition
        return best_item
        
    def swap_best_by_category (self, other, my_priority, their_priority):
        other_item = other.best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if my_item == None or other_item == None:
            return False
        else: 
            self.swap_items(other, my_item, other_item)
            return True


# Vendors have a method named get_best_by_category, which will get the item with the best condition in a certain category
# It takes one argument: a string that represents a category
# This method looks through the instance's inventory for the item with the highest condition and matching category
# It returns this item
# If there are no items in the inventory that match the category, it returns None
# It returns a single item even if there are duplicates (two or more of the same item with the same condition)



# In Wave 1 we will create the `Vendor` class.

# - There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
# - Inside this module, there is a class named `Vendor`
# - Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
# - When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`


# - Every instance of `Vendor` has an instance method named `add`, which takes in one item
# - This method adds the item to the `inventory`
# - This method returns the item that was added

# - Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
# - This method removes the matching item from the `inventory`
# - This method returns the item that was removed
# - If there is no matching item in the `inventory`, the method should return `False`


# - Instances of `Vendor` have an instance method named `get_by_category`
#   - It takes one argument: a string, representing a category
#   - This method returns a list of `Item`s in the inventory with that category