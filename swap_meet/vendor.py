from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        items_by_category = []

        for item in self.inventory:
            if category == item.category:
                items_by_category.append(item)
        return items_by_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.inventory.remove(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)
        return True 

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None

        max_item = max(items_in_category, key=lambda item: item.condition)
        return max_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_given_to_other = self.get_best_by_category(their_priority)
        item_given_to_me = other.get_best_by_category(my_priority)
        if not item_given_to_me or not item_given_to_other:
            return False

        return self.swap_items(other, item_given_to_other, item_given_to_me)



