# ### Wave 1

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

from pickle import FALSE


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory 

    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item
    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False 
        else:
            self.inventory.remove(removed_item)
            return removed_item  
