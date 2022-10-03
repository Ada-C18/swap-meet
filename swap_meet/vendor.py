class Vendor:
    def __init__(self, inventory = None):
        
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
            
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item:
            return False
        
        self.inventory.remove(item)
        return item