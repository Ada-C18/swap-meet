class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory != None else []
      
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in another_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            return True
        else:
            return False
