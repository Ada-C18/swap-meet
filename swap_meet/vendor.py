from operator import inv
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item) 
        return item_list
    
    def swap_items(self, friend_list, my_item, their_item):
        if my_item in self.inventory:
            if their_item in friend_list.inventory:
                friend_list.remove(their_item)
                friend_list.add(my_item)
                self.add(their_item)
                self.remove(my_item)
                return True
            else:
                return False
        else:
            return False

    def swap_first_item(self, friend_list):
        if len(self.inventory) !=0:
            if len(friend_list.inventory) !=0:
                self.swap_items(friend_list,self.inventory[0], friend_list.inventory[0])
                return True
            else:
                return False
        else:
            return False

    def get_best_by_category(self, category):
        best_item = None
        best_condition = -1
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        swap_is_happening = False

        their_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)

        if their_best_item and my_best_item:
            swap_is_happening = True
            self.remove(my_best_item)
            other.remove(their_best_item)
            self.add(their_best_item)
            other.add(my_best_item)
    
        return swap_is_happening
            
