from operator import itemgetter
from typing import ItemsView

from .item import Item


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
        items_list =[]
        for item in self.inventory:
            if item.get_category() == category:
                items_list.append(item)
        return items_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False
