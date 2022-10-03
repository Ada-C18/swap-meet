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
        self.inventory.remove(item)
        return item
