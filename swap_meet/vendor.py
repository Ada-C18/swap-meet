# import item to access Item class in Vendor class
from swap_meet.item import Item

#creat Vendor class has __init__ , add , remove , get_by_category, wap_items, exciting_inventory function
class Vendor:
    def __init__(self, inventory= None):
        if inventory is None:
            inventory =[]
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
        #or
        # if item in self.inventory:
        #     return True
        # else:
        #     return False
    

    def swap_first_item(self,friend):
        #If either itself or the friend have an empty inventory return False
        if not self.inventory or not friend.inventory:
            return False
        #use swap_items(), removes the first item from its inventory, and adds the friend's first item
        #removes the first item from the friend's inventory, and adds the instances first item
        return self.swap_items(friend, self.inventory[0],friend.inventory[0])
            
            
