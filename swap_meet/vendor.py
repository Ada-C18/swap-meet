from operator import truediv
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = list()):
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