class Vendor:
    
    def __init__(self,inventory):
        self.inventory = []
        self.inventory_list = inventory
    
    
def add(self,item):
        self.inventory_list.append(item)
        return item
def remove(self,item_to_remove):
        if item_to_remove not in self:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        