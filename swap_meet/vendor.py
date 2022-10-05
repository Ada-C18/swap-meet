from pickle import FALSE
from swap_meet import item
# from item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        # self.item = item   

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)   
            return item
        else:
            return False
    
    def get_by_category(self,category):
        items = []
        self.category = category
        if self.category == item.self.category:
            items.append(item.self.category)
        
        else:
            return None    
        
    # def swap_items():
