class Vendor:
    def __init__(self, inventory=[]):
        # inventory is an empty list by default
        # we can optionally pass in a list with the keyword argument inventory
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)

    def remove(self, item):
        '''
        Input: item
        Ouput: item that was removed, or False if no matching item in list
        Method removes the matching item from the inventory
        '''
        # remove() method removes the first occurrence of the element with the specified value
        # If you need to remove an item by its index number and/or for some reason you want to return (save) the value you removed, use the pop() method instead.
        if item in self.inventory:
            self.inventory.pop(item)
            return item
        else:
            # If there is no matching item in the inventory, the method should return False
            return False
