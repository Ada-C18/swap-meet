class Vendor:
    def __init__(self, inventory = []):
        self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        self.inventory.remove(item) #is .remove the real thing to use
        return item