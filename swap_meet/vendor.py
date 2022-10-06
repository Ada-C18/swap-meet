
from operator import attrgetter
from swap_meet.item import Item
from swap_meet.decor import Decor
class Vendor:
    
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_by_category = [item for item in self.inventory if item.category == category]
        return items_by_category        

    def swap_items(self, my_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in my_friend.inventory:
            return False 
        self.inventory.remove(my_item)
        my_friend.inventory.append(my_item)
        my_friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True 

    def swap_first_item(self, my_friend):
        if self.inventory == [] or my_friend.inventory == []:
            return False 
        self.inventory[0] , my_friend.inventory[0] = my_friend.inventory[0] , self.inventory[0]
        return True
        

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0:
            return None 
        best_item = max(items_by_category, key=attrgetter('condition'))
        return best_item
    

