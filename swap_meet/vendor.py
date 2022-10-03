from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory= None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item  
        return None

    def get_by_category(self, category):
        things_in_category = []
        for thing in self.inventory:
            if thing.category == category:
                things_in_category.append(thing)
        return things_in_category
    
    def swap_items(self, vendor_2, item_1, item_2):
        if item_1 in self.inventory and item_2 in vendor_2.inventory:
        # take first item from first vendor and give to other
            self.inventory.remove(item_1)
            vendor_2.inventory.append(item_1)
        # take second item from second vendor and give to other
            vendor_2.inventory.remove(item_2)
            self.inventory.append(item_2)
            return True
        
        return False