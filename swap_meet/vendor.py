class Vendor:
    def __innit__(self, inventory=None):
        self.inventory = inventory

    def add(self, item):
        self.item = item
        inventory = inventory if inventory is not None else []
        inventory.append(item)
        return inventory