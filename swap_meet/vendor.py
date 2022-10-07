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
        """
        Expectation: Every instance of Vendor has an instance method named add. This method adds the item to the inventory
        Input: takes in one item. 
        Output: This method returns the item that was added"""
        
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        """ Expectation: This method removes the matching item from the inventory
        Input: takes in one item.
        Output: This method returns the item that was removed. If there is no matching item in the inventory, the method should return False"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

################################## Wave 2 ##################################
    
    def get_by_category(self,category = ""):
        """ 
        Expectation: Instances of Vendor have an instance method named get_by_category
        Input: Takes one argument: a string, representing a category
        Output: This method returns a list of Items in the inventory with that category"""
        list = []
        
        # for item in self.inventory:
        #     if item.category == category:
        #         list.append(item)
        # return list

        list = [item for item in self.inventory if item.category == category]
        return list
    
 ################################## Wave 3 ##################################   
 
    def swap_items(self,vendor,my_item,their_item):
        """Input: It takes 3 arguments:
        an instance of another Vendor, representing the friend that the vendor is swapping with
        an instance of an Item (my_item), representing the item this Vendor instance plans to give
        an instance of an Item (their_item), representing the item the friend Vendor plans to give
        Output: It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
        It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
        It returns True
        If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False"""
        
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
        """
        Expectation: This method considers the first item in the instance's inventory, and the first item in the friend's inventory
        It removes the first item from its inventory, and adds the friend's first item
        It removes the first item from the friend's inventory, and adds the instances first item
        It returns True
        If either itself or the friend have an empty inventory, the method returns False
        Input: It takes one argument: an instance of another Vendor, representing the friend that the vendor is swapping with
        Output: True or False """
                
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
