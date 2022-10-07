from operator import contains, truediv
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = list()
        self.inventory = inventory
    
    def add(self, item):
        """
        Returns the item that is added to the inventory.
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Returns the matching item and removes it from the inventory.
        If there is no matching item, return False.
        """
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        """
        Returns a list of Items in the inventory with given category.
        """
        item_list = list()
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list
    
    def swap_items(self, other, my_item, their_item):
        """
        Swaps this Vendor's my_item with the other Vendor's their_item. 
        Returns True if swap is successful.
        Returns False, if this Vendor's inventory doesn't contain my_item
        or the other Vendor's inventory doesn't contain their_item.
        """
        if my_item in self.inventory and their_item in other.inventory:
            return self.swap(other, my_item, their_item)
        return False
    
    def swap_first_item(self, other):
        """
        Swaps this Vendor's first item with the other Vendor's first item.
        Returns True if swap is successful.
        Returns False, if either this Vendor or the other Vendor have an empty inventory.
        """
        if self.inventory and other.inventory:
            return self.swap(other, self.get_item_by_index(0), other.get_item_by_index(0))
        return False
    
    def get_best_by_category(self, category):
        """
        Returns the item with the highest condition and matching category from the inventory.
        """
        best_item, best_condition = None, -1
        for item in self.inventory:
            if item.category.lower() == category.lower() and item.condition > best_condition:
                best_item = item
                best_condition = item.condition
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps this Vendor's best item whose category matches their_priority with 
        the other Vendor's best item whose category matches my_priority.
        Returns True if swap is successful.
        Returns False, if either this Vendor or the other Vendor have no item matching the given category.
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if my_item and their_item:
            return self.swap(other, my_item, their_item)
        return False
    
    def get_newest(self):
        """
        Returns the item with the minimum age from the inventory.
        Returns None if age is not specified.
        """
        newest_item, minimum_age = None, float('inf')
        for item in self.inventory:
            if item.age < minimum_age:
                newest_item = item
                minimum_age = item.age
        return newest_item
    
    def swap_by_newest(self, other):
        """
        Swaps this Vendor's nwest item with the other Vendor's newest item.
        Returns True if swap is successful.
        Returns False, if either this Vendor or the other Vendor have an empty inventory.
        """
        my_item = self.get_newest()
        their_item = other.get_newest()
        if my_item and their_item:
            return self.swap(other, my_item, their_item)
        return False

#======================================#        
#========== Helper Functions ==========#
#======================================#  
    def get_item_by_index(self, index):
        """
        Returns the item at the given index in the inventory.
        """
        try:
            return self.inventory[index]
        except IndexError:
            raise IndexError("The index is out of range of the inventory list.")
        
    def swap(self, other, my_item, their_item):
        """
        Removes the my_item from this Vendor's inventory, and adds it to the friend's inventory.
        Removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
        Returns True when swap is completed.
        """
        self.add(other.remove(their_item))
        other.add(self.remove(my_item))
        return True
