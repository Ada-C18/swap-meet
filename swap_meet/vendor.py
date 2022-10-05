from nis import cat
from .item import Item

class Vendor:
    def __init__(self, inventory=None) -> None:
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            self.remove(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            self.add(friend.inventory.pop(0))
            friend.add(self.inventory.pop(0))
            return True