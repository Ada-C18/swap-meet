from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
        
    def get_by_category(self,category):
        category_items = [item for item in self.inventory if item.category == category]
        return category_items
    
    def swap_items(self, vendor, my_item, their_item):
        my_inventory = self.inventory 
        their_inventory = vendor.inventory

        if my_item not in my_inventory or their_item not in their_inventory:
            return False

        my_inventory.remove(my_item)
        my_inventory.append(their_item)
        their_inventory.remove(their_item)
        their_inventory.append(my_item)
        return True
