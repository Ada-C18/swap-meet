
from swap_meet.item import Item

#Wave1

class Vendor:
    """
    A class to represent a vendor with inventory. 
    """

    def __init__(self, inventory = None):
        """
        Constructs inventory attribute for the vendor object,
        which is an empty list by default.
        """

        if inventory is None:
            inventory = []
        self.inventory = inventory
                
    def add(self, item):
        """
        Returns the item added to inventory.
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Returns the removed matching item from the inventory 
        or False if no matching item in the inventory.
        """
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    # Wave 2
    
    def get_by_category(self, category = ""):
        """
        Returns a list of Items in the inventory with that category.
        """
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    #Wave #3

    def swap_items(self, friend_vendor, my_item = "", their_item = ""):
        """
        Returns True if my_item and their_item from this and
        friend's vendor inventories are swapped.
        """
        if my_item in self.inventory and their_item in friend_vendor.inventory: 
            self.remove(my_item)
            friend_vendor.add(my_item)
            friend_vendor.remove(their_item)
            self.add(their_item)
            return True
        
    
    #Wave 4

    def swap_first_item(self, friend_vendor):
        """
        Returns True if the first item from this inventory and
        the first item from friend's vendor inventories are swapped.
        """
        if not self.inventory or not friend_vendor.inventory:
            return False
        self.swap_items(friend_vendor, self.inventory[0],friend_vendor.inventory[0])
        return True

    #Wave 6

    def get_best_by_category(self, category):
        """
        Returns the item with the highest condition and matching category;
        or None if no items in the inventory that match the category.
        """
        items_by_category = self.get_by_category(category)
        if not items_by_category:
            return None
        
        best_item = max(items_by_category,key=lambda x:x.condition)
        return best_item

    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Returns True if the best item in my inventory that matches 
        their_priority category is swapped with the best item in 
        other's inventory that matches my_priority.
        """
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        
        if my_best_item is None or their_best_item is None:
            return False
        
        self.swap_items(other, my_best_item, their_best_item)
        return True
        




    

        


        
        


