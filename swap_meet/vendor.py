class Vendor:
    
    def __init__(self, inventory=[]):
        # we can also do none or false using if else
        self.inventory = inventory 
    def add(item):
        self.inventory.append(item)
        return item
    def remove(item):
        for inventory_item in inventory:
            if inventory_item==item:
                self.inventory.remove(item)
                return item
        return False