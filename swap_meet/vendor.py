from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category (self, category):
        if not category:
            return None
        matching_items = []
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            first_own = self.inventory[0]
            first_friend = friend.inventory[0]
            self.swap_items(friend, first_own, first_friend)
            return True
        return False

    def get_best_by_category(self, category):
        inventory = self.get_by_category(category)
        if not inventory:
            return None
        highest = 0
        best_item = None
        for item in inventory:
            if item.condition > highest:
                highest = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.swap_items(other, my_best, their_best)
        return True