class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return self.inventory[-1]

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            removed_item = self.inventory.pop(self.inventory.index(item_to_remove))
            return removed_item
        else:
            return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, swapper, my_item, their_item):
        swapper.add(self.inventory.pop(self.inventory.index(my_item)))
        self.add(swapper.inventory.pop(swapper.inventory.index(their_item)))
        return True
