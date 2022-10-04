class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else [] 

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 
    
    def get_by_category(self, category): 
        items_list = []
        
        for item in self.inventory:
            if category == item.category:
                items_list.append(item)
        
        return items_list
    
    def swap_items(self, vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        vendor.inventory.append(self.inventory.pop(self.inventory.index(my_item)))
        self.inventory.append(vendor.inventory.pop(vendor.inventory.index(their_item)))
        
        # self.inventory.remove(my_item)
        # other_vendor.inventory.append(my_item)
        # self.inventory.append(their_item)
        # other_vendor.inventory.remove(their_item)
        
        return True

