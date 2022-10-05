from operator import attrgetter
from swap_meet.item import Item

class Vendor:
    
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
        #another way of writing the if statement:
        #if not bool(self.inventory) or not bool(vendor.inventory)
        if not self.inventory or not vendor.inventory: #check for empty list and return False
            return False
        else:
            self.swap_items(vendor,self.inventory[0],vendor.inventory[0])
            return True
    
    def get_best_by_category(self,category):
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
            
    def swap_best_by_category(self,other,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other,my_best_item,their_best_item)
        return True
