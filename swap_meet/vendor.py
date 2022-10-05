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

