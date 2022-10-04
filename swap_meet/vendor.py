from operator import attrgetter
from swap_meet.item import Item

class Vendor:
    # def __init__(self,inventory = []):
    #     self.inventory = inventory
    
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self,category = ""):
        list = []
        
        for item in self.inventory:
            if item.category == category:
                list.append(item)
        return list
    
    
    def swap_items(self,vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.add(their_item)
            vendor.add(my_item)
            self.remove(my_item)
            vendor.remove(their_item)
            return True

    def swap_first_item(self,vendor):
        if not self.inventory or not vendor.inventory: #check for empty list and return False
            return False
        else:
            self.swap_items(vendor,self.inventory[0],vendor.inventory[0])
            vendor.swap_items(vendor,vendor.inventory[0],self.inventory[0])
            return True
#Need to investigate why this does not work
        # if bool(self.inventory) or bool(vendor.inventory):
        #     return False
        # else: 
        #     self.swap_items(vendor,self.inventory[0],vendor.inventory[0])
        #     vendor.swap_items(vendor,vendor.inventory[0],self.inventory[0])
        #     return True
    
    def get_best_by_category(self,category):
        
        # highest_condition = max(condition_list, key=lambda Vendor: Vendor.condition)
        # max = max(condition_list, key = attrgetter("condition"))
        # print("########################",condition_list[0].item.condition)
        # if (len(self.inventory)) == 0:
        #     return None
        # else:
        #     best_condition = max(self.inventory, key=lambda x:x.condition)
        #     print(best_condition)
        #     return best_condition
        # highest_condition = max(condition_list, key)
        if len(self.inventory) == 0:
            return None
        
        
        condition_list = self.get_by_category(category)
        if len(condition_list) == 0:
            return None
        else:
            best_condition = 0
            best_item = 0
            for item in condition_list:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
            return best_item
            
                