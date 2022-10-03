class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
        self.inventory = self.inventory if inventory is not None else []
    
    def add(self, item):

        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory: 
            item_removed = item
            self.inventory.remove(item) 
            return item_removed
        else:
            return False