from re import I
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        '''A blueprint for different store inventories.'''
        if inventory is None:
            inventory = [] 
        self.inventory = inventory
    
    def add(self, item):
        '''Add an item to the inventory list.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Remove an item from inventory list.'''
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        '''Return a list of items in the inventory with category.'''
        category_list = [i for i in self.inventory if i.category == category]
        return category_list
            
    def swap_items(self, other_vendor, my_item, their_item):
        '''Remove an item from this Vendor's inventory and swaps
        with other vendor.'''
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        return True
      

    def swap_first_item(self, other_vendor):
        '''Swap the first item in this vendor's inventory with
        first item of other vendor.'''
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        '''Returns item with the best condition in a certain category.'''
        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None
        best_item = max(items_in_category, key=lambda item: item.condition)
        
        return best_item
        
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Swap best item of certain categories with another vendor.'''
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        
        if my_item is None or their_item is None:
            return False
        self.swap_items(other, my_item, their_item)
        return True
