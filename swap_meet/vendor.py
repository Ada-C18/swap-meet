from operator import itemgetter
from typing import ItemsView

from .item import Item


class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
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
    
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        first_item = self.inventory[0]
        friend_frist_item = friend.inventory[0]
        return self.swap_items(friend, first_item, friend_frist_item)
        
    
    def get_best_by_category(self, category):
        highest_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category and item.condition >= highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)
        return self.swap_items(other, my_best_item, their_best_item)
        