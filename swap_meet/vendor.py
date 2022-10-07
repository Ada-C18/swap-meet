from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

# adds item to inventory
    def add(self, item):
        self.inventory.append(item)
        return item 

# removes item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

# returns list of items that match by category
    def get_by_category (self, category):
        if not category:
            return None
        matching_items = []
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items

# swaps item that you want + item that your friend wants from each inventory, if each inventory contains it.
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            return True
        return False

# swaps items, but specifically the first items of each inventory.
    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            first_own = self.inventory[0]
            first_friend = friend.inventory[0]
            self.swap_items(friend, first_own, first_friend)
            return True
        return False

# loops through a list of items matching requested category and outputs the item with the highest condition.
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

# finds best condition item in a category you want and a category your friend wants.
# if either doesn't have item, returns false. otherwise, swaps those two items.
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.swap_items(other, my_best, their_best)
        return True