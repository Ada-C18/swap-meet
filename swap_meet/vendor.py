class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return self.item