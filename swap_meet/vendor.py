from operator import contains, truediv
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = list()) -> None:
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
    
    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Removes the my_item from this Vendor's inventory, and adds it to the friend's inventory.
        Removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
        Returns True when above actions are completed.
        Returns False, if this Vendor's inventory doesn't contain my_item
        or the friend's inventory doesn't contain their_item. the method returns False
        """
        if self.contain(my_item) and friend_vendor.contain(their_item):
            self.add(friend_vendor.remove(their_item))
            friend_vendor.add(self.remove(my_item))
            return True
        return False

#========== Helper Functions ==========#
    
    def contain(self, item) -> bool:
        """
        Returns True if the inventory contains the given item, otherwise False.
        """
        return item in self.inventory
    
