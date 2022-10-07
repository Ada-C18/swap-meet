from xmlrpc.client import INVALID_ENCODING_CHAR

from attr import s

class Vendor:
    def __init__(self, inventory = None):
        # inventory is a empty list
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item



    def get_by_category(self, str_category):
        category_list = []
        for string in self.inventory:
            if string.category == str_category:
                category_list.append(string)
        return category_list



    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or\
           their_item not in another_vendor.inventory:
           # another_vendor.inventory --> (parameter_name.attribute_name)
            return False

        another_vendor.inventory.append(self.remove(my_item))
        another_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
   
        # self.inventory.remove(my_item)
        # another_vendor.inventory.append(my_item)
        # another_vendor.inventory.remove(their_item)
        # self.inventory.append(their_item)

        return True


    def swap_first_item(self, another_vendor):
        if self.inventory == [] or another_vendor.inventory == []:
            return False

        my_item = self.inventory[0]
        their_item = another_vendor.inventory[0]
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        another_vendor.inventory.remove(their_item)
        another_vendor.inventory.append(my_item)
        
        return True


    def get_best_by_category(self, str_category):
        category_list = self.get_by_category(str_category)
        # call the get_by_category funtion and assign to a variable
        if len(category_list) == 0:
            return None 
        best_condition = category_list[0]
        for item in category_list:
            if item.condition > best_condition.condition:
                best_condition = item
                # will only get the first one that appear with the best condition
        return best_condition


    def swap_best_by_category(self, other, my_priority, their_priority):
        # other, which represents another Vendor instance to trade with
        # my_priority, which represents a category that the Vendor wants to receive
        # their_priority, which represents a category that other wants to receive
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.swap_items(other, my_best, their_best)
        return True




        


            
        
        
        
            
            


