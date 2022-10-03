
# =========================WAVE 1==============================================

# create a vendor class

class Vendor:

# each vendor will have INVENTORY attribute
# instantiate an instance of VENDOR we can optionally pass in a list for INVENTORY--> inventory=[]

    def __init__(self, inventory=[]):
        self.inventory = inventory

# every instance of vendor has ADD instance method
# ADDs one item to inventory
# returns the item that was added

    def add(self, item):
        self.inventory.append(item)
        return item

# every instance of vendor has REMOVE instance method
# REMOVEs one item from inventory
# this method removes the "matching" item from inventory
# returns the item that was removed

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

# IF no matching items in INVENTORY, return False