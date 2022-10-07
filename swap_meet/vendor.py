class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            removed_item = self.inventory.pop(self.inventory.index(item_to_remove))
            return removed_item
        return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            # Pops each item from their respective inventories and swaps them using Vendor.add()
            other.add(self.inventory.pop(self.inventory.index(my_item)))
            self.add(other.inventory.pop(other.inventory.index(their_item)))
            return True
        return False

    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            self.swap_items(other, self.inventory[0], other.inventory[0])
            return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if category_list:
            return max(category_list, key=lambda item: item.condition)
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        if self.inventory and other.inventory:
            my_item_choice = other.get_best_by_category(my_priority)
            their_item_choice = self.get_best_by_category(their_priority)
            if my_item_choice and their_item_choice:
                self.swap_items(other, their_item_choice, my_item_choice)
                return True
        return False

    def swap_by_newest(self, other):
        if self.inventory and other.inventory:
            self_newest_item = min(self.inventory, key=lambda item: item.age)
            other_newest_item = min(other.inventory, key=lambda item: item.age)
            self.swap_items(other, self_newest_item, other_newest_item)
            return True
        return False
