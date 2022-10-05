from operator import itemgetter
from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
        
    
    def add(self, item):
    
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            print(self.inventory)
            if item.category == category:
                items_list.append(item)
        return items_list
     

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        elif my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True 

# In Wave 4 we will write one method, `swap_first_item`.

# - Instances of `Vendor` have an instance method named `swap_first_item`
#   - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
#   - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
#   - It removes the first item from its `inventory`, and adds the friend's first item
#   - It removes the first item from the friend's `inventory`, and adds the instances first item
#   - It returns `True`
#   - If either itself or the friend have an empty `inventory`, the method returns `False`

    def swap_first_item (self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False 
        elif self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0]):
            return True 
