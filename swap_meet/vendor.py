from swap_meet.item import Item


class Vendor:
    def __init__(self,inventory=[]):
        self.inventory = inventory

    def add(self,item):
        self.item = item
        self.inventory.append(item)
        return self.item
    
    def remove(self,item):
        self.item = item
        if item not in self.inventory:
            return False
        elif item in self.inventory: 
            self.inventory.remove(item)
        return self.item
    def get_by_category(self,category=""):
        item_list=[]
        for item in self.inventory:
            if item.category==category:
                item_list.append(item)
        return item_list
        
        




