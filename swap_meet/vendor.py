from xmlrpc.client import INVALID_ENCODING_CHAR

########### wave 1 ###########
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



    ########### wave 2 ###########
    def get_by_category(self, str_category):
        category_list = []
        for string in self.inventory:
            if string.category == str_category:
                category_list.append(string)
        return category_list



    ########### wave 3 ############
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


    ########### wave 4 ############
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


        


            
        
        
        
            
            


