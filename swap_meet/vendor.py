from pickle import FALSE
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory=None):
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

    def get_by_category(self, category_name):
        list_item = []
        for item in self.inventory:
            if category_name == item.category:
                list_item.append(item)
        return list_item

# friend_vendor = Vendor()
# my_vendor = Vendor()
# their_item = Item()
# my_item = Item()

# friend_vendor.get_by_category(friend_inventory)
# my_vendor.get_by_category(my_inventory)
# Wave 3
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.remove(my_item)
            friend_vendor.add(my_item)
            self.add(their_item)
            friend_vendor.remove(their_item)
            return True
        return False

# Wave 4
    def swap_first_item(self, friend_vendor):
        if len(friend_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
        first_inventory = self.inventory[0]
        friend_first = friend_vendor.inventory[0]
        self.swap_items(friend_vendor, first_inventory, friend_first)
        # self.remove(first_inventory)
        # friend_vendor.add(first_inventory)
        # self.add(friend_first)
        # friend_vendor.remove(friend_first)
        return True

# Wave 6
    def get_best_by_category(self, category_name):
        category_items = []
        for item in self.inventory:
            if item.category == category_name:
                category_items.append(item)

        if len(category_items) == 0:
            return None
        else:
            best_condition = category_items[0].condition
            best_item = category_items[0]
            for item in category_items:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
            return best_item
# other -> represents another Vendor
# my_priority, their_priority -> a category wants to receive
    def swap_best_by_category(self, other, my_priority, their_priority):
        other_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if my_best in self.inventory and other_best in other.inventory:
            self.swap_items(other, my_best, other_best)
            # self.add(other_best)
            # self.remove(my_best)
            # other.add(my_best)
            # other.remove(other_best)
            return True
        return False
