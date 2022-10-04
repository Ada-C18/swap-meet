

class Vendor:
    
    def __init__(self, inventory = None):
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
        else:
            return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, other_inventory, my_item, their_item):
        if their_item in other_inventory.inventory and my_item in self.inventory:
            other_inventory.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            other_inventory.inventory.append(my_item)
        else:
            return False
        return self.inventory

    def swap_first_item(self, other_inventory):
        if self.inventory and other_inventory.inventory:
            my_first = self.inventory[0]
            their_first = other_inventory.inventory[0]
            other_inventory.inventory.remove(their_first)
            self.inventory.append(their_first)
            self.inventory.remove(my_first)
            other_inventory.inventory.append(my_first)
        else:
            return False
        return self.inventory

    def get_best_by_category(self, category):
        best_condition = 0
        best_item = ""
        category_items = self.get_by_category(category)
        if not category_items:
            best_item = None
        else:
            for item in category_items:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_swap = self.get_best_by_category(their_priority)
        their_swap = other.get_best_by_category(my_priority)
        if not self.inventory or not other.inventory:
            return False
        elif my_swap not in self.inventory or their_swap not in other.inventory:
            return False
        else:
            self.swap_items(other, my_swap, their_swap)
        return self.inventory


