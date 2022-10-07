from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items 

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)
        vendor.remove(their_item)
        vendor.add(my_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])


    def get_best_by_category(self, category):
        # best_condition = 0
        # best_item = None

        # for item in self.get_by_category(category):
        #     if item.condition > best_condition:
        #         best_condition = item.condition
        #         best_item = item

        # return best_item

        items = self.get_by_category(category)
        if not items:
            return None
        return max(items, key = lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.get_by_category(their_priority) or not other.get_by_category(my_priority):
            return False

        item_to_give = self.get_best_by_category(their_priority)
        item_to_recieve = other.get_best_by_category(my_priority)

        return self.swap_items(other, item_to_give, item_to_recieve)

