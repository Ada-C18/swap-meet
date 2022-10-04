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
    
    def swap_items(self, vendor, my_item, their_item):
        self.vendor = vendor # friend vendor is swapping with 
        self.item = my_item # item vendor is giving away 
        self.item = their_item # their friend is giving away  

        if my_item in self.inventory: 
            self.remove(my_item) 
            vendor.add(my_item) 
        if their_item in vendor.inventory:
            vendor.remove(their_item)
            self.add(their_item)
        return True

        


    
        
        




