from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False

        self.remove(my_item)
        another_vendor.add(my_item)
        another_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, another_vendor):
        if not self.inventory or not another_vendor.inventory:
            return False

        self_first = self.inventory.pop(0)
        another_first = another_vendor.inventory.pop(0)
        self.inventory.append(another_first)
        another_vendor.inventory.append(self_first)
        return True










    