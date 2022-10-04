class Vendor:
    '''add doc string'''
    def __init__(self, inventory=[]):
        print(f"🎃 {inventory}")
        self.inventory = inventory  # list of item objects

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        inventory_by_category = []
        for item in self.inventory:  # items in inventory have categories
            if item.category == category:
                inventory_by_category.append(item)
        return inventory_by_category      

    def swap_items(self, another_vendor, my_item, their_item):
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        if my_item in self.inventory and their_item in another_vendor.inventory:
            print(f"BEFORE {self.inventory=}")
            self.add(their_item)
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            print(f"AFTER {self.inventory=}")
            return True
        return False
        

