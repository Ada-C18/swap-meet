from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

        
    def add(self,item):
        
        self.inventory.append(item)
        return item 
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False 
    
    def get_by_category(self,category):
        # return a list of "items" in the inventory with that category
        list_of_items = []
        for item in self.inventory:
            if category == Item.category:
                list_of_items.append(item)
                
        return list_of_items

