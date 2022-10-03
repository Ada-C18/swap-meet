from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        '''A blueprint for different store inventories.'''
        # inventory is a list
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = [] 
    
    def add(self, item):
        '''Add an item to the inventory list.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Remove an item from inventory list.'''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        category_list = []
        for i in self.inventory:
            if i.category == category:
                category_list.append(i)
        return category_list
            

