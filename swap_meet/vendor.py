class Vendor:
    def __init__(self, inventory = None):
        
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
            
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item:
            return False
        elif item not in self.inventory:
            return False    
        
        self.inventory.remove(item)
        return item

    def get_by_category(self,item,category):
        if item in self.category:
            return self.inventory