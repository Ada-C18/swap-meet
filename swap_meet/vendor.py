from pickle import FALSE
from swap_meet.item import Item

class Vendor:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        return item

    def remove_item(self, item):
        if item in self.inventory:
            return item
        return False