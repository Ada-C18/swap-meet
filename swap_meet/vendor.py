class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        self.inventory.remove(item)
        if item not in self.inventory:
            return False
        return item

