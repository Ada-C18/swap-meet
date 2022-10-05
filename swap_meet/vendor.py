from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        merch =[]
        for item in self.inventory:
            if item.category is category:
                merch.append(item)
        return merch

    def swap_items(self, vendor2, my_item, their_item):
        self.vendor2 = vendor2
        self.my_item = my_item
        self.their_item = their_item

        # how do I call add, remove?