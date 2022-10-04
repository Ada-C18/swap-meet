from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    
# default list error here (inventory= None)

    def add(self, item):
        self.inventory.append(item)
        return item 
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
        
    def get_by_category(self, category):
        list_of_category_match = []
        for i in self.inventory:
            if i.category == category:
                list_of_category_match.append(i)
        return list_of_category_match
        
