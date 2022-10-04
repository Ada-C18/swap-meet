from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory= []):
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