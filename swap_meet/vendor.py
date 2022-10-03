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
