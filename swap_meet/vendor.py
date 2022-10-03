class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        return self.inventory.append(item) 
    
    def remove(self, item):
        matching_item = item
        self.inventory.remove(matching_item)
        
    
Vendor(inventory = None)        