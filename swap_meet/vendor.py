class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or list()
        
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False