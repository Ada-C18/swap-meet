class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory

    def add(self, new_item):
        self.inventory(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
        return item_to_remove