class Vendor:
    def __init__(self, inventory = None):
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
        categories = []
        for item in self.inventory:
            if item.category == category:
                categories.append(item)
        return categories

    def swap_items(self, vendor1, my_item, their_item):
        #vendor1 = Vendor()
        if my_item in self.inventory and their_item in vendor1.inventory:
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            vendor1.inventory.append(my_item)
            vendor1.inventory.remove(their_item)
            return True
        return False



        
