class Vendor:
    def __init__(self, inventory=None):
      self.inventory = inventory if inventory is not None else []   

    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item


    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False 
        
        self.inventory.remove(removed_item)
        return removed_item  


    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if category == item.category:
                items.append(item)
        return items
    

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True


    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0: 
            return False 
      
        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True


    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best_item = ''
        best_condition = 0
        for item in items:
            if item.condition > best_condition:
                best_item = item 
                best_condition = item.condition 
        return best_item

        
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item_to_swap = self.get_best_by_category(their_priority)
        others_item_to_swap = other.get_best_by_category(my_priority)
        if my_item_to_swap is None or others_item_to_swap is None:
            return False 
        
        self.swap_items(other, my_item_to_swap, others_item_to_swap)
        return True
