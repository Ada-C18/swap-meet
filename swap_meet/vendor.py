from swap_meet.item import Item

class Vendor:
    #optionally pass in argument "inventory"
    def __init__(self, inventory = None):
        # if "inventory" arugment is passed in, use that
        if inventory:
            self.inventory = inventory
        # otherwise, if there's no inventory argument, initialize and empty list
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False

# do I need to import Item in order for this part of 
# the function to work?
    def get_by_category(self, category):
        inventory_categories = []
        for item in self.inventory:
            if item.category == category:
                inventory_categories.append(item)
        return inventory_categories