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
<<<<<<< HEAD
    
    def get_by_category(self, category):
        filtered_list = []
        for item in self.inventory:
            if item.get_category() == category:
                filtered_list.append(item)
        return filtered_list

=======
        
    def get_by_category(self, category):
        items_list =[]
        for item in self.inventory:
            if item.get_category() == category:
                items_list.append(item)
        return items_list

    def swap_items(self, friend, my_item, their_item):
        pass
>>>>>>> 20f29eebc8654f4bb5fc94ae0655806d90d063f6
