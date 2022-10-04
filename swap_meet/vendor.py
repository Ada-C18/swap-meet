# import item to access Item class in Vendor class
from swap_meet.item import Item

#creat Vendor class has __init__ , add , remove , get_by_category, wap_items, exciting_inventory function
class Vendor:
    def __init__(self, inventory= []):
        self.inventory = inventory
    
    def add(self,item):
        # this function add item to inventory list
        self.inventory.append(item)
        return item
    def remove(self, item):
        # this function remove item into inventory
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self,category):
        #create list and if item,category equal category add item to list
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

    def swap_items(self, friend, my_item, their_item):
        
        if not self.exciting_inventory(my_item):
            return False
        elif not friend.exciting_inventory(their_item):
            return False
        else:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
            
    def exciting_inventory(self, item):
        #if item in self.inventory return True
        return item in self.inventory




        # if item in self.inventory:
        #     return True
        # else:
        #     return False

        
            
            
