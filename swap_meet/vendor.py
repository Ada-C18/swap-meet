from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item
    
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        
        self.inventory.remove(remove_item)
        return remove_item
    
    def get_by_category(self, item_category):
        items_list = [item for item in self.inventory if item.category == item_category]

        return items_list
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        friend.add(self.remove(my_item))
        self.add(friend.remove(their_item))
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    
import copy
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        shared_category = []
        for item in self.inventory:
            if item.category == category:
                shared_category.append(item)
        return shared_category

    def swap_items(self, Vendor, my_item, their_item ):
        if my_item in self.inventory and their_item in Vendor.inventory:
            self.add(Vendor.remove(their_item))
            Vendor.add(self.remove(my_item))
            return True
        return False

    def swap_first_item(self, Vendor):
        if self.inventory and Vendor.inventory:
            return self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
        return False
        
    

    def get_best_by_category(self, category):
        category = self.get_by_category(category)
        if not category:
            return None
        return max(category, key=lambda item: item.condition)



def swap_best_by_category(self, other, my_priority, their_priority):
    my_item = other.get_best_by_category(my_priority)
    their_item = self.get_best_by_category(their_priority)
    self.swap_items(my_item, their_item)

# def swap_by_newest(self, other):
#     their_item = min(other.inventory, key=lambda item: item.age)
#     my_item = min(other.inventory, key=lambda item: item.age)
