class Vendor:
    def __init__(self,inventory=None):
        self.inventory = inventory if inventory is not None else [] 

    def add(self,item):
        self.item = item
        self.inventory.append(item)
        return self.item
    
    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 

