from pickle import FALSE
from swap_meet import item
# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        # self.item = item   

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)   
            return item
        else:
            return False
        
    # wave_2
    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list

    # wave_3 
    def swap_items(self, swapping_other_vendor, my_item, their_item):  
        if my_item in self.inventory and their_item in swapping_other_vendor.inventory:
                self.remove(my_item)
                self.add(their_item)
                swapping_other_vendor.add(my_item)
                swapping_other_vendor.remove(their_item)
                return True
        else:
            return False


    # Wave_4
    
