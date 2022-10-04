'''
module: vendor.py
    class: Vendor
        attribute: .inventory
        mothod: .add .remove
'''

from .item import Item

class Vendor:

    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else: # default
            self.inventory = []

    def add(self, one_item):
    # add the item to the inventory
        new_inventory = self.inventory.append(one_item)
        return one_item
    
    def remove(self, one_item):
        if one_item in self.inventory:
            new_inventory = self.inventory.remove(one_item)
            return one_item
        else:
            return False

    def get_by_category(self, category): # category in str
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in another_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            self.add(their_item)
            return True
         