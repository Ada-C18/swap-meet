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
        self.vendor = vendor 
        self.my_item = my_item # this vendor giving away 
        self.their_item = their_item # their friend giving away  

        for my_item in self.inventory: 
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item) 
        for their_item in vendor.inventory:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else: 
            return True 


    
        
        




