from swap_meet.item import Item


class Vendor:

    def __init__(self, inventory=None):
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
        inventory_by_cat_list = [
            item for item in self.inventory if item.category == category]

        return inventory_by_cat_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.add(their_item)
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)

        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        self.swap_items(friend, self.inventory[0], friend.inventory[0])

        return True

    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None

        return max(self.get_by_category(category), key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False

        self.swap_items(other, my_item, their_item)
        return True


# ------ EXTRA ------


    def swap_by_newest(self, other):
        if not self.inventory or not other.inventory:
            return False

        my_newest = min(self.inventory, key=lambda item: item.age)
        their_newest = min(other.inventory, key=lambda item: item.age)

        self.swap_items(other, my_newest, their_newest)
        return True
