class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
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
    
    def swap_items(self, vendor1, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor1.inventory:
            return False
        self.remove(my_item)
        vendor1.add(my_item)
        vendor1.remove(their_item)
        self.add(their_item)
        return True
