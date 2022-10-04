class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if getattr(item, 'category') == category:
                items_list.append(item)
        return items_list