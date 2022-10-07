from distutils.command.build_scripts import first_line_re


class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category = ""):
        item_category_list = []
        for item in self.inventory:
            if item.category == category:
                item_category_list.append(item)
        return item_category_list
            
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            self.add(vendor.remove(vendor.inventory[0])) 
            vendor.add(self.remove(self.inventory[0]))
            return True

    def get_best_by_category(self, category = ""):
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None

        best_condition = 0
        best_item = []
        for item in category_list:
            if item.condition > best_condition:
                best_item = [item]
                best_condition = item.condition
            elif item.condition == best_condition:
                best_item.append(item)

        return best_item[0]

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if their_best_item in other.inventory and my_best_item in self.inventory:
            self.inventory.append(their_best_item)
            other.inventory.append(my_best_item)
            other.inventory.remove(their_best_item)
            self.inventory.remove(my_best_item)
            return True
        else:
            return False



