from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
            
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, friend, my_item, their_item):  
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        friend.inventory.append(my_item)
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    def get_best_by_category(self, category):
        return max(self.get_by_category(category), key = lambda item: item.condition, default = None)

    def swap_best_by_category(self, other, my_priority, their_priority):
        return self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))