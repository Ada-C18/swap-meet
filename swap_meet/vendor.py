class Vendor:
    
    def __init__(self, inventory=None):
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
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if their_item not in vendor.inventory or my_item not in self.inventory:
            return False

        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        instance_first_item = self.inventory[0]
        vendor_first_item = vendor.inventory[0]
        self.remove(instance_first_item)
        self.add(vendor_first_item)
        vendor.remove(vendor_first_item)
        vendor.add(instance_first_item)
        return True


