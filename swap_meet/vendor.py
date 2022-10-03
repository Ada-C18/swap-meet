class Vendor:
    
    def __init__(self, inventory):
        # self.inventory = inventory
        if len(inventory) >= 1:
            self.inventory = inventory
        else:
            self.inventory = []            
# default list error here (inventory= None)

    def add(self, item):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        for item in self.inventory:
            if item in self.inventory:
                self.inventory.remove(item)
                return item

        return False
        
    


