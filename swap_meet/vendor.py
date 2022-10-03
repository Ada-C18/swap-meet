class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        index = len(self.inventory) - 1
        return self.inventory[index]

    def remove(self, item):
        self.inventory.remove(item)
        return item