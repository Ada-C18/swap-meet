class Vendor:
    def __init__(self, inventory = None, item):
        self.inventory = inventory if inventory is not None else []
        self.item = item

    def add(self, item):
        self.inventory.append(item) 
        return item
    
    def remove(self, item):
        matching_item = item
        if item not in self.inventory:
            return False
        self.inventory.remove(matching_item)
        return matching_item

    def get_by_category(self, category):
        item_list = self.item(self.category)
        return item_list
    
Vendor(inventory = None)        