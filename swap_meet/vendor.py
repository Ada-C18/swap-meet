class Vendor:
    
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item