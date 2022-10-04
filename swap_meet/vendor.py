from operator import itemgetter
from typing import ItemsView

from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        filtered_list = []
        for item in self.inventory:
            if item.get_category() == category:
                filtered_list.append(item)
        return filtered_list

