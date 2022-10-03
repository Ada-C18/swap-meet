from xmlrpc.client import INVALID_ENCODING_CHAR

from pytest import Item


class Vendor:
    def __init__(self, inventory = []):
        # inventory is a empty list
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, str_category):
        category_list = []
        for string in self.inventory:
            if string.category == str_category:
                category_list.append(string)
        return category_list
       

            
        
        
        
            
            


