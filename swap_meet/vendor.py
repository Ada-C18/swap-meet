'''
module: vendor.py
    class: Vendor
        attribute: .inventory
        method: .add .remove .get_by_category .swap_items .swap_first_item
'''

from swap_meet.item import Item

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
         
    def swap_first_item(self, another_vendor):
        if not self.inventory or not another_vendor.inventory: 
            return False
        else:
            temp1 = self.inventory[0]
            temp2 = another_vendor.inventory[0]
            self.inventory[0] = temp2
            another_vendor.inventory[0] = temp1
            return True

    def get_best_by_category(self, category):
        ref_condition = 0
        item_highest = None
        if not self.inventory:
            return None
        for item in self.inventory:
            if item.category == category and item.condition >= ref_condition:
                ref_condition = item.condition
                item_highest = item
        return item_highest

    def swap_best_by_category(self, other, my_priority, their_priority): # priority: category

        my_best_item_they_want = self.get_best_by_category(their_priority) 
        their_best_item_i_want = other.get_best_by_category(my_priority) 
        if not my_best_item_they_want or not their_best_item_i_want:
            return False
        else: 
            self.swap_items(other, my_best_item_they_want, their_best_item_i_want)
            return True