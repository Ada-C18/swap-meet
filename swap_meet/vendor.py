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
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        self.add(friend.inventory.pop(0))
        friend.add(self.inventory.pop(0))
        return True

    def get_best_by_category(self, category):
        categories = self.get_by_category(category)
        if not categories:
            return None 
        best_item = categories[0]
        for item in categories:
            if item.condition > best_item.condition:
                best_item = item
        return  best_item

    # def swap_best_by_category(self, other, my_priority, their_priority):
        