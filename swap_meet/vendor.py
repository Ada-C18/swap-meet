class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    def add(self, item):
        
        self.inventory.append(item)
        return self.item

