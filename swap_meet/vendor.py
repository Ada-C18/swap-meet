from re import L


class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    
# default list error here (inventory= None)

    def add(self, item):
        self.inventory.append(item)
        return item 
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
        

