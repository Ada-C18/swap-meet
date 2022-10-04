# relative import
# from .item import Item

# full import
from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        # inventory is an empty list by default
        # we can optionally pass in a list with the keyword argument inventory
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''
        Input: item
        Ouput: item that was removed, or False if no matching item in list
        Method removes the matching item from the inventory
        '''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, input_category):
        ''' 
        Input: a string, representing a category
        Output: returns a list of Items in the inventory with that category
        '''
        category_items = []

        for item in self.inventory:
            if item.category == input_category:
                category_items.append(item)
        return category_items
