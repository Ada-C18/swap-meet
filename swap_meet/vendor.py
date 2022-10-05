class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def get_by_category(self, category):
        return list(filter(lambda item: item.category == category, self.inventory))

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

