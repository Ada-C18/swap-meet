class Vendor:
    # def __init__(self, inventory = []):
    # By having MUTABLE TYPE in DEFAULT argument, HAVE PROBLEMS in INTERGRATION TEST ISSUE
    # default value none is immutable. mutable xx

    def __init__(self, inventory = None):    
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
