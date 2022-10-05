class Vendor:
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        vendor.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        their_first_item = vendor.inventory[0]
        my_first_item = self.inventory[0]
        first_item_swap = self.swap_items(vendor, my_first_item, their_first_item)
        return first_item_swap

    def get_best_by_category(self, category):
        condition_list = self.get_by_category(category)

        best_value = 0
        best_item = None
        if not condition_list:
            return False
        for item in condition_list:
            if item.condition > best_value:
                best_value = item.condition
                best_item = item
        return best_item

    
    
    