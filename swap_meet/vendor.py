from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        index = len(self.inventory) - 1
        return self.inventory[index]

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, old_item, new_item):
        self.inventory.remove(old_item)
        self.inventory.append(new_item)
        vendor.inventory.remove(new_item)
        vendor.inventory.append(old_item)
        return True