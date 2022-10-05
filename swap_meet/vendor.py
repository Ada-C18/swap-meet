
from swap_meet.item import Item

#Wave1

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
                
    def add(self, item):
        """
        Returns the item added to inventory
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

    def swap_items(self, friend_vendor, my_item = "", their_items = ""):
        """
        Returns True if my_item was moved from this Vendor's inventory
        to the friend's inventory and their_item was moved from the
        other Vendor's inventory, and added it to this Vendor's inventory.
        """
        if my_item in self.inventory and their_items in friend_vendor.inventory: 
            self.remove(my_item)
            friend_vendor.add(my_item)
            friend_vendor.remove(their_items)
            self.add(their_items)
            return True
        
    
    #Wave 4

    def swap_first_item(self, friend_vendor):
        """
        Returns .....
        """
        if not self.inventory  or not friend_vendor.inventory:
            return False
        removed_first = self.remove(self.inventory[0])
        friend_vendor.add(removed_first)
        removed_friends_first = friend_vendor.remove(friend_vendor.inventory[0])
        self.add(removed_friends_first)
        return True

    #Wave 6

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        if not items_by_category:
            return None
        # best_item = max(items_by_category, key = attrgetter('condition'))
        
        # Another way to find max from attributes of object's list
        best_item = max(items_by_category,key=lambda x:x.condition)
            
        # best_cond = 0
        # best_item = items_by_category[0]
        # for item in items_by_category:
        #     if item.condition > best_cond:
        #         best_cond = item.condition
        #         best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        
        if my_best_item is None or their_best_item is None:
            return False
        else:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        




    

        


        
        


