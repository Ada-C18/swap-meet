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

    def get_by_category(self, category):
        items_list = []

        for item in self.inventory:
            if category == item.category:
                items_list.append(item)

        return items_list

    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        vendor.inventory.append(self.inventory.pop(self.inventory.index(my_item)))
        self.inventory.append(vendor.inventory.pop(vendor.inventory.index(their_item)))

        return True

    def swap_first_item(self, vendor):

        if not self.inventory or not vendor.inventory:
            return False

        vendor_item = vendor.inventory.pop(0)
        self.inventory.append(vendor_item)

        my_item = self.inventory.pop(0)
        vendor.inventory.append(my_item)

        return True
