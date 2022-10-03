class Vendor:
    '''add doc string'''
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        inventory_by_category = []
        for item in self.inventory:
            if item.category == category:
                inventory_by_category.append(item)
        return inventory_by_category      
