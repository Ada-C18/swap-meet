class Vendor:
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
