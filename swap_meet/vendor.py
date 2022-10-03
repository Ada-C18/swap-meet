from logging import raiseExceptions


class Vendor:
#   Initiate the class 'Vendor'
#   Attribute 'Inventory' = empty list
#   Intance method #1: add
#       - return item that was added
#   Instance method #2: remove
#       - takes in (1) item
#       - removes matching item from inventory
#       - returns the item that was removed-- .pop()
#       - if no matching item in inventory, return False

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            raise exception("False")
        return item