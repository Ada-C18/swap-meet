import pytest


class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    #return a list of items that the vendor has in a given category  
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)

        return category_list

    """
    Swap_items vendor method removes and adds items from both vendor's inventories.
    """
    def swap_items(self, other_vendor, my_item, their_item):
        #remove
        self.remove(my_item)
        other_vendor.remove(their_item)
        #add
        self.add(their_item)
        other_vendor.add(my_item)

        return True