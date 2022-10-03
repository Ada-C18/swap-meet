class Vendor:
    # define __init__ class ,takes inventory as a 
    # parameter. Inventory default == None

    # if not inventory initialize an empty list

    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else: 
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item

        except ValueError:
            return False



    