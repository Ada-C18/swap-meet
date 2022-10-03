class Vendor:
    
    def __init__(self, inventory=[]):
        # we can also do none or false using if else
        self.inventory = inventory 
    def add(self,item):
        self.inventory.append(item)
        return item
    def remove(self,item):
        for inventory_item in self.inventory:
            if inventory_item==item:
                self.inventory.remove(item)
                return item
        return False
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item == category:
                item_list.append(item)
        return item_list


