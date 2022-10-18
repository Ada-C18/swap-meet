class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item
    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

