
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
#-------------Wave2--------------------------- 
    def get_by_category(self,category_name):
        list =[item for item in self.inventory if item.category == category_name]
        return list
#-------------Wave3--------------------------- 
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False
#-------------Wave4--------------------------- 
    def swap_first_item(self,friend):
        if not self.inventory or not friend.inventory:
            return False
        self.swap_items(friend,self.inventory[0],friend.inventory[0])
        # friend.inventory.append(self.inventory[0])
        # self.inventory.append(friend.inventory[0])
        # self.inventory.pop(0)
        # friend.inventory.pop(0)
        return True
#-------------Wave6--------------------------- 
    def get_best_by_category(self,category_name):
        if not self.get_by_category(category_name):
            return None
        return max(self.get_by_category(category_name), key =lambda item:item.condition) 
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best=other.get_best_by_category(my_priority)
        my_best=self.get_best_by_category(their_priority)
        
        if not self.get_by_category(their_priority) or not other.get_by_category(my_priority):
            return False
        
        self.swap_items(other, my_best, their_best)
        return True
#-------------optional---------------------------
    
    def swap_by_newest(self, other):
        my_newest=min(self.inventory, key =lambda item:item.age) 
        their_newest=min(other.inventory, key =lambda item:item.age) 
        #if it's the same age, no swap

        self.swap_items(other,my_newest,their_newest)
        return True