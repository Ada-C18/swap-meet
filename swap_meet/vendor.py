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
<<<<<<< HEAD

#Wave 3
    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            my_swap = my_item
            their_swap = their_item
            self.add(their_swap)
            self.remove(my_item)
            vendor.add(my_swap)
            vendor.remove(their_item)
        return True

=======
    
>>>>>>> 2ab0b8ba9c2455653540b0accb488eb3cd68262d
    def swap_items(self, other_vendor, my_item,their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            other_vendor.add(my_item)
            self.inventory.append(their_item)
            other_vendor.remove(their_item)
            return True
        
<<<<<<< HEAD
=======

>>>>>>> 2ab0b8ba9c2455653540b0accb488eb3cd68262d
#Wave 4
    def swap_first_item(self, other_vendor):
        if len(self.inventory)<1 or len(other_vendor.inventory) < 1:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True

            # swap = self.inventory[0]
            # self.inventory[0] = vendor.inventory[0]
            # vendor.inventory[0] = swap
            # return True
            
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True


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