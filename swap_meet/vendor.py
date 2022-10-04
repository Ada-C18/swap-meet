class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    
    def swap_items(self, another_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in another_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        another_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        another_vendor.inventory.remove(their_item)
        return True

    def swap_first_item(self, another_vendor):
        if not self.inventory or not another_vendor.inventory:
            return False
        #my_first_item = self.inventory.pop(0)
        another_vendor.inventory.append(self.inventory.pop(0))
        #their_first_item = another_vendor.inventory.pop(0)
        self.inventory.append(another_vendor.inventory.pop(0))
        return True