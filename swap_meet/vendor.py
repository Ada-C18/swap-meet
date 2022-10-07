# from operator import attrgetter
from swap_meet.item import Item

################################## Wave 1 ##################################
class Vendor:
    """ Each Vendor will have an attribute named inventory, which is an empty list by default
When we instantiate an instance of Vendor, we can optionally pass in a list with the keyword argument inventory """
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self,item):
        """Every instance of Vendor has an instance method named add, which takes in one item. This method adds the item to the inventory
        This method returns the item that was added"""
        
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        """E very instance of Vendor has an instance method named remove, which takes in one item. This method removes the matching item from the inventory
This method returns the item that was removed. If there is no matching item in the inventory, the method should return False"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

################################## Wave 2 ##################################
    
    def get_by_category(self,category = ""):
        list = []
        
        # for item in self.inventory:
        #     if item.category == category:
        #         list.append(item)
        # return list

        list = [item for item in self.inventory if item.category == category]
        return list
    
 ################################## Wave 3 ##################################   
 
    def swap_items(self,vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.add(their_item)
            vendor.add(my_item)
            self.remove(my_item)
            vendor.remove(their_item)
            return True


################################## Wave 4 ##################################

    def swap_first_item(self,vendor):        
        if not self.inventory or not vendor.inventory: #OR #if not bool(self.inventory) or not bool(vendor.inventory)
            return False
        else:
            self.swap_items(vendor,self.inventory[0],vendor.inventory[0])
            return True
    
    def get_best_by_category(self,category):
        try:
            best_item = max(self.get_by_category(category), key = lambda x:x.condition)
            return best_item
        except:
            return None
        
        #Solution 2 using loop
            # best_condition = 0
            # best_item = 0
            # for item in condition_list:
            #     if item.condition > best_condition:
            #         best_condition = item.condition
            #         best_item = item
            
            #solution 3 using attrgetter
            # best_item = max(condition_list, key = attrgetter('condition'))
            
            
    def swap_best_by_category(self,other,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other,my_best_item,their_best_item)
        return True
