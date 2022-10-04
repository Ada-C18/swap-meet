class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.item = item
        self.inventory.append(self.item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(self.item)
            return self.item

    def get_by_category(self, category):
        items_filtered_by_category = []   

        for item in self.inventory:
            if item.category == category:
                items_filtered_by_category.append(item)

        return items_filtered_by_category
            
vendor1 = Vendor([])