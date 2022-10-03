from .item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        if self.inventory == []:
            self.inventory = [item]
        else:
            self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        items = [single_item for single_item in self.inventory if category == single_item.category]
        return items
        # items = []
        # for single_item in self.inventory:
        #     if category == single_item.category:
        #         items.append(single_item) 
        # return items