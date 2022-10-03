class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return self.inventory[-1]

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            removed_item = self.inventory.pop(self.inventory.index(item_to_remove))
            return removed_item
        else:
            return False
