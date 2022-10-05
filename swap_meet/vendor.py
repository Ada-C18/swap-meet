from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item
    
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        
        self.inventory.remove(remove_item)
        return remove_item
    
    def get_by_category(self, item_category):
        items_list = [item for item in self.inventory if item.category == item_category]

        return items_list
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        friend.add(self.remove(my_item))
        self.add(friend.remove(their_item))
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    def get_best_by_category(self, category):
        category = self.get_by_category(category)
        if not category:
            return None

        return max(category, key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_new_item = other.get_best_by_category(my_priority)
        their_new_item = self.get_best_by_category(their_priority)

        return self.swap_items(other, their_new_item, my_new_item)

    def swap_by_newest(self, other):
        if not self.inventory or not other.inventory:
            return False
        my_newest_item = min(self.inventory, key=lambda item: item.age)
        other_newest_item = min(other.inventory, key=lambda item: item.age)
        return self.swap_items(other, my_newest_item, other_newest_item)