
class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category): 
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            vendor.remove(self.add(their_item))
            vendor.add(self.remove(my_item))
            return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        else:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            # self.add(vendor.remove(vendor.inventory[0]))
            # vendor.add(self.remove(self.inventory[0]))
            return True
        
    def get_best_by_category(self, category):
        best_condition = -1
        best_item = None
        
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.get_by_category(their_priority) or not other.get_by_category(my_priority):
            return False
        else:
            self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))
            return True    