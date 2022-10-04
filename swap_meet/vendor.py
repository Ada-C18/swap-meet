from swap_meet.item import Item
# from item import Item  #using for debugging - ask why
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
        


