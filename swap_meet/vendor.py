class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    # adds an item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # removes an item from the inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    # takes one argument (string => category) and returns a list of items in the
    # in the inventory with that category
    def get_by_category(self, category):
        all_items = []
        for item in self.inventory:
            if item.category == category:
                all_items.append(item)
        return all_items

    # swaps items between 2 vendors' inventories
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

    # move my_item from my inventory to theirs
        self.remove(my_item)
        other_vendor.add(my_item)

    # move their_item from their inventory to mine
        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(
            other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

# Vendors have a method named get_best_by_category, which will get the item with the best condition in a certain category
    def get_best_by_category(self, category):
        if not self.inventory:
            return None
        best_item = min(self.inventory, key = lambda item: item.condition)
        return best_item

# Vendors have a method named swap_best_by_category, which will swap the best item of certain categories with another Vendor
