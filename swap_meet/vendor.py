from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        items_by_category = []
        
        for item in self.inventory:
            if category == item.category:
                items_by_category.append(item)
        return items_by_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.inventory.remove(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)
        return True 