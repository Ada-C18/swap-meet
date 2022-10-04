from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        list_by_category = []
        
        # I don't know what else to call it... so it's thing for now =/
        for thing in self.inventory:
            if thing.category == category:
                list_by_category.append(thing)
        return list_by_category
