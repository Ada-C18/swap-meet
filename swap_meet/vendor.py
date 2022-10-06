class Vendor:
    def __init__(self, inventory=None):
        # set inventory if it is provided, or set to empty list
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    # returns a list of items in the inventory from given category
    def get_by_category(self, category):
        all_items = []
        for item in self.inventory:
            if item.category == category:
                all_items.append(item)
        return all_items

    # swaps items between 2 vendors' inventories, returns True if item was swapped
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    # swaps first item, returns True if swapped
    def swap_first_item(self, other_vendor):
        # if either inventory is empty, return False
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(
            other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    # returns item with best condition for a certain category
    def get_best_by_category(self, category):

        all_items_in_cat = self. get_by_category(category)

        # if no items are in the given category, return None
        if not all_items_in_cat:
            return None

        best_item = max(all_items_in_cat, key=lambda item: item.condition)
        return best_item

    # returns True if swap happened
    def swap_best_by_category(self, other, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        # returns None if a vendor doesn't have an item in preferred category
        if not my_best_item or not their_best_item:
            return None

        self.swap_items(other, my_best_item, their_best_item)
        return True
