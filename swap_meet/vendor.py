class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    #adds an item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    #removes an item from the inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item


