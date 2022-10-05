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
        

    def swap_first_item(self, another_vendor):

        if len(self.inventory) > 0 and len(another_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = another_vendor.inventory[0]
            return self.swap_items(another_vendor, my_item, their_item)

        else:
            return False

            
    def get_best_by_category(self, category):

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
        
        # create category lists for self and other
        other_categories = []
        my_categories = []
        for item in other.inventory:
            other_categories.append(item.category)

        for item in self.inventory:
            my_categories.append(item.category)

        if my_priority in other_categories and their_priority in my_categories:
            my_best_by_category = self.get_best_by_category(their_priority)
            their_best_by_category = other.get_best_by_category(my_priority)

            other.add(my_best_by_category)
            self.remove(my_best_by_category)

            self.add(their_best_by_category)
            other.remove(their_best_by_category)
            
            return True
        
        else:
            return False
            

