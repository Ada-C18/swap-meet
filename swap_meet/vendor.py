# from .item import Item # actually, you don't need to import Item

class Vendor:
    def __init__(self, inventory = None):
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
        category_items = [item for item in self.inventory
            if item.category == category]
        return category_items
    
    def swap_items(self, vendor, my_item, their_item):
        my_inventory = self.inventory 
        their_inventory = vendor.inventory

        if my_item not in my_inventory or their_item not in their_inventory:
            return False

        my_inventory.append(their_item)
        their_inventory.append(my_item)
        my_inventory.remove(my_item)
        their_inventory.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        my_inventory = self.inventory 
        their_inventory = vendor.inventory

        if not my_inventory or not their_inventory:
            return False

        my_item = my_inventory[0]
        their_item = their_inventory[0]
        return self.swap_items(vendor, my_item, their_item)

    def get_best_by_category(self, category):
        # best_item = None
        # for item in self.inventory:
        #     if item.category == category:
        #         if best_item is None:
        #             best_item = item
        #         elif item.condition > best_item.condition:
        #             best_item = item
        # return best_item
        try:
            return max(self.get_by_category(category),
                key = lambda item: item.condition)
        
        except ValueError:
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False

        self.swap_items(other, my_best, their_best)
        return True