from tkinter import N
from xml.dom.expatbuilder import theDOMImplementation
from swap_meet.item import Item

class Vendor(Item):
    '''Creating vendor with inventory. Includes methods for adding and removing
    items from inventory by category and condition. Includes methods for swapping
    items by category and condition.'''
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory  # list of item objects

    def add(self, item):
        '''Add item to inventory list.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Remove item from inventory list.'''
        if item in self.inventory:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        '''Get item from inventory by category.'''
        inventory_by_category = []
        
        for item in self.inventory:  # items in inventory have categories
            if item.category == category:
                inventory_by_category.append(item)

        return inventory_by_category      

    def swap_items(self, another_vendor, my_item, their_item):
        '''Swap item between self and another vendor. Call add and remove
        methods.'''
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        
        if my_item in self.inventory and their_item in another_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            return True
        
        return False
        

    def swap_first_item(self, another_vendor):
        '''Swap first item in self inventory with first item in another
        vendor's inventory.'''
        if len(self.inventory) > 0 and len(another_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = another_vendor.inventory[0]
            return self.swap_items(another_vendor, my_item, their_item)

        else:
            return False

            
    def get_best_by_category(self, category):
        '''Get item in best condition by category.'''
        best_item_condition = 0.0
        best_item_count = 0
        
        for item in self.inventory:
            if item.category == category:
                best_item_count += 1
                if item.condition > best_item_condition:
                    best_item_condition = item.condition

        for item in self.inventory:
            if item.condition == best_item_condition and item.category == category:

                return item
        
        if best_item_count == 0:
            return None
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Swap item in best condition by desired category of other vendor 
        and vice versa. Returns False if desired category not in either
        inventory.'''
        my_best_by_category = self.get_best_by_category(their_priority)
        their_best_by_category = other.get_best_by_category(my_priority)

        if my_best_by_category and their_best_by_category:
            self.swap_items(other, my_best_by_category, their_best_by_category)
            
            return True

        else:
            return False

###############Extra#################            
    
    # def get_newest_item(self, age):
    #     '''Get newest item.'''
    #     newest_age = max(self.inventory, key=lambda: self.age)
    #     return self.inventory.newest_age
        

    # def swap_by_newest(self, other, my_newest, their_newest):
    #     my_newest = self.get_newest_item
    #     their_newest = other.get_newest_item
    #     print(f"{my_newest=}")
    #     print(f"{their_newest=}")
    #     self.swap_items(other, my_newest, their_newest)
