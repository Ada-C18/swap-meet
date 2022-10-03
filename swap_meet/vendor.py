from logging import raiseExceptions
from typing_extensions import Self

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []


    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items
        # items = []
        # if not self.inventory: # If inventory is empty, return an empty list.  
        #     return items
        # for item in self.inventory:
        #     if item.category == category:
        #         items.append(item)

        # return items
        
    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        another_vendor.inventory.append(my_item)
        another_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True



        

            
        