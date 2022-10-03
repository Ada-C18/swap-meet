class Vendor:
    def __init__(self, inventory= None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, vendor, item_a, item_b):
        if (item_a not in self.inventory or item_b not in vendor.inventory):
            return False

        self.inventory.remove(item_a)
        self.inventory.append(item_b)
        vendor.inventory.remove(item_b)
        vendor.inventory.append(item_a)
        return True
    
    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
            
        self.inventory.append(vendor.inventory[0])
        vendor.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        vendor.inventory.remove(vendor.inventory[0])
        return True