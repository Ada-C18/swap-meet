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

    def get_by_category(self, category):

        items_list = [item for item in self.inventory if category == item.category]

        return items_list

    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        vendor.inventory.append(self.inventory.pop(self.inventory.index(my_item)))
        self.inventory.append(vendor.inventory.pop(vendor.inventory.index(their_item)))

        return True

    def swap_first_item(self, vendor):

        if not self.inventory or not vendor.inventory:
            return False

        return self.swap_items(vendor, my_item=self.inventory[0], their_item=vendor.inventory[0])

    def get_best_by_category(self, category):

        if all(item.category is not category for item in self.inventory):
            return None

        condition = 0
        highest_item = None
        items_list = self.get_by_category(category)

        for item in items_list:
            if item.condition > condition:
                condition = item.condition
                highest_item = item
        return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        return self.swap_items(other, my_item, their_item)
