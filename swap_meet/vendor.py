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

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if their_item not in vendor.inventory or my_item not in self.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)
        vendor.remove(their_item)
        vendor.add(my_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        instance_first_item = self.inventory[0]
        vendor_first_item = vendor.inventory[0]
        return self.swap_items(vendor, instance_first_item, vendor_first_item)

    def get_best_by_category(self, category_str):
        highest_item_pair = (-1.0, None)
        for item in self.inventory:
            if item.category == category_str and item.condition > highest_item_pair[0]:
                highest_item_pair = (item.condition, item)
        return highest_item_pair[1]

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best is None or their_best is None:
            return False
        return self.swap_items(other, my_best, their_best)




