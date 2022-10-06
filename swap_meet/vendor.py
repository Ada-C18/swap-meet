from cmath import exp
from multiprocessing.sharedctypes import Value
from swap_meet import item


class Vendor:
    # init attributes: inventory(list)
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    # method to add items to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
        
    # method to remove items from inventory
    def remove(self, item):
        try:
            self.inventory.remove(item)
        except(ValueError):
            return False

        return item
   
    # iterates through inventory and puts into seperate list based on category attribute
    def get_by_category(self, category):
        filter = []
        for item in self.inventory:
            if item.category == category:
                filter.append(item)

        return filter 
        
    def swap_items(self, other_vendor, self_item, other_item):
        
        try:
            index_1 = self.inventory.index(self_item)
            index_2 = other_vendor.inventory.index(other_item)
        except(ValueError):
            return False 
        
        self.inventory.append(other_vendor.inventory.pop(index_2))
        other_vendor.inventory.append(self.inventory.pop(index_1))
        return True

            
    def swap_first_item(self, other_vendor):
        try:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        except(IndexError):
            return False

    def get_best_by_category(self, category):
        try:
            return max(self.get_by_category(category), key=lambda i: i.condition)
        except(ValueError):
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):

        trade_happened = self.swap_items(other, self.get_best_by_category(their_priority),
        other.get_best_by_category(my_priority))

        return trade_happened
        




        


        