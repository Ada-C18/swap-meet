from swap_meet.item import Item
class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return self.item

    
    def get_by_category(self, category):
        # return [item for item in self.inventory if item.category == category]
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list
       