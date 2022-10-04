from xml.dom.expatbuilder import theDOMImplementation
from swap_meet.item import Item

class Vendor(Item):
    '''add doc string'''
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory  # list of item objects

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        inventory_by_category = []
        
        for item in self.inventory:  # items in inventory have categories
            if item.category == category:
                inventory_by_category.append(item)
        
        return inventory_by_category      

    def swap_items(self, another_vendor, my_item, their_item):
        
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        
        if my_item in self.inventory and their_item in another_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            return True
        
        return False
        

### Wave 4

    def swap_first_item(self, another_vendor):

        if len(self.inventory) > 0 and len(another_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = another_vendor.inventory[0]
            return self.swap_items(another_vendor, my_item, their_item)

        else:
            return False

### Wave 6
            
    def get_best_by_category(self, category):
        self.best_item = 0.0
        best_item_count = 0
        
        for item in self.inventory:
            if item.category == category:
                best_item_count += 1
                if item.condition > self.best_item:
                    self.best_item = item.condition

        for item in self.inventory:
            if item.condition == self.best_item:
                return item
        
        if best_item_count == 0:
            return None
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        if my_priority == other.get_best_by_category and their_priority == self.get_best_by_category:
            self.inventory.add(my_priority)
            self.inventory.remove(their_priority)
            other.add(their_priority)
            other.remove(my_priority)
        else:
            return False

