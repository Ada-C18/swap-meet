from .clothing import Clothing
from .decor import Decor
from .electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        friend.inventory.append(my_item)
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        self.inventory.remove(my_item)
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        my_first = self.inventory[0]
        their_first = friend.inventory[0]
        return self.swap_items(friend, my_first, their_first)
        
    
    def get_best_by_category(self, category):
        ranked_inventory = sorted(self.inventory, key = lambda i: i.condition, reverse = True)
        for item in ranked_inventory:
            if item.category == category:
                return item
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        giving = self.get_best_by_category(their_priority)
        receiving = other.get_best_by_category(my_priority)
        return self.swap_items(other, giving, receiving)