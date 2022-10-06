from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category ==item.category:
                list_of_items.append(item)
        return list_of_items
    
    def swap_items(self,friends_vendor, my_item,their_item):
        if my_item not in self.inventory or their_item not in friends_vendor.inventory:
            return False

        friends_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        friends_vendor.inventory.append(my_item)

        return True
    
    def swap_first_item(self , friends_vendor):
        if len(self.inventory)==0 or len(friends_vendor.inventory)==0 :
            return False
        w=self.inventory[0]
        self.inventory.remove(self.inventory[0])
        self.inventory.append(friends_vendor.inventory[0])
        friends_vendor.inventory.remove(friends_vendor.inventory[0])
        friends_vendor.inventory.append(w)
        return True

    def get_best_by_category(self,category):
        category_list=[]
        for item in self.inventory:
            if  item.category==category:
                category_list.append(item)
        if len(category_list)==0:
            return None
        best_item=category_list[0]
        best_item_condition=best_item.condition
    
        for item in category_list:
            if item.condition > best_item_condition:
                best_item=item
                best_item_condition=item.condition
        return best_item   

    def swap_best_by_category(self,other,my_priority,their_priority):
        self_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if self_best_item == None or their_best_item == None:
            return False
        return self.swap_items(other,self_best_item,their_best_item)
            
