from swap_meet.item import Item
class Vendor:

    def __init__(self,inventory = None):
        if inventory is None:
            inventory =[]
        
        self.inventory = inventory
     

    def add(self,item):
        self.inventory.append(item)  
        return item

    def remove(self,item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item 

    def get_by_category(self,category):
        list_items =[]

        for item in self.inventory:
            if item.category == category:
                list_items.append(item)

        return list_items   


    def swap_items(self,friend,my_item,their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        return False 

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory :
            return False
        self.swap_items(friend, self.inventory[0],friend.inventory[0])
        return True  



    def get_best_by_category(self, category):
        highest_condition =0
        highest_item =None
        items_list = self.get_by_category(category)
        for item in items_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_item = item

        return highest_item        


    def swap_best_by_category(self,other,my_priority,their_priority):
        my_best_item = other.get_best_by_category(my_priority) 
        their_best_item = self.get_best_by_category(their_priority) 
        return self.swap_items(other,their_best_item,my_best_item)



        ############### Optional Enhancements  ##############





       








        