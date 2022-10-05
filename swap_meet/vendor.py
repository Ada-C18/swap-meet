from operator import attrgetter

#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items
        
    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        another_vendor.inventory.append(my_item)
        another_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True

    def swap_first_item(self, another_vendor):
        if not self.inventory or not another_vendor.inventory:
            return False
        self.inventory[0], another_vendor.inventory[0] = another_vendor.inventory[0], self.inventory[0]
        return True

#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_best_by_category(self, category):
        list_items_by_category = self.get_by_category(category)
        return max(list_items_by_category, key=attrgetter('condition')) if list_items_by_category else None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        else:
            return False
