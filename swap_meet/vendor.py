# from pickle import FALSE
# from operator import invert
# from unittest import result
# from swap_meet import item
from operator import ne
from swap_meet.item import Item

class Vendor:
    """ Object: create a profile with the inventory and some features of each item"""
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        """ Append new items to the current inventory"""
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """ Remove one item to the current inventory"""
        if item in self.inventory:
            self.inventory.remove(item)   
            return item
        else:
            return False
        
    # wave_2
    def get_by_category(self, category):
        """ Get a list of items with the same category"""
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list

    # wave_3 
    def swap_items(self, swapping_other_vendor, my_item, their_item):
        """ Swap items, remove items from the original inventory and add it to other person's inventory"""
        if my_item in self.inventory and their_item in swapping_other_vendor.inventory:
                self.remove(my_item)
                swapping_other_vendor.remove(their_item)
                self.add(their_item)
                swapping_other_vendor.add(my_item)
                return True
        else:
            return False

    # Wave_4
    def swap_first_item(self, swapping_other_vendor):
        """Swap the first item in the inventory"""
        if self.inventory == [] or swapping_other_vendor.inventory == []:
            return False
        
        self.swap_items(swapping_other_vendor, self.inventory[0], swapping_other_vendor.inventory[0])
        return True
        
    # Wave_6
    
    def get_best_by_category(self, category):
        """Return the item with the hightest condition per category"""
        inventory_items_category = self.get_by_category(category) #list
        if inventory_items_category == []:
            return None

        highest_item = inventory_items_category[0]
        for item in inventory_items_category:
            if item.condition >= highest_item.condition:
                highest_item = item
        return highest_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swap the desire category items from the inventories """
        if self.inventory == [] or other == []:
            return False
        
        my_priority_item = other.get_best_by_category(my_priority)  # item
        their_priority_item = self.get_best_by_category(their_priority) #item
        
        if my_priority_item in other.inventory and their_priority_item in self.inventory:
            return self.swap_items(other, their_priority_item, my_priority_item)
            
        return False
    
    # Optional Enhancements
    
    def get_newest(self):
        pass
        if self.item.age == None:
            return None

        my_newest_item = min(self.inventory, key=lambda i:i[age])
        return my_newest_item

    
    def swap_by_newest(self, age):
        pass
    