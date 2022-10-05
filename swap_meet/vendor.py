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
        # self.category = category    # no needed
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list


    # wave_3  


















#     # wave_3  
#     def swap_items(self, ):
        
# #pending!!
#     def swap_items(self, swapping_vendor, my_item, their_item):
#             """given another vendor, my_item to swap, their_item to receive, make that swap."""
#             #if each item is in the right place, make the swap:
#             if my_item in self.inventory and their_item in swapping_vendor.inventory:
#                 #make the swap
#                 self.remove(my_item)
#                 self.add(their_item)
#                 swapping_vendor.add(my_item)
#                 swapping_vendor.remove(their_item)
#                 return True
#             else:
#                 return False



