class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def get_by_category(self, category):
        return list(filter(lambda item: item.category == category, self.inventory))

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        return True
