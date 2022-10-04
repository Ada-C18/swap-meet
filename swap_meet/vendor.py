
# =========================WAVE 1==============================================
# from unicodedata import category
from swap_meet.item import Item

# create a vendor class


class Vendor():

# each vendor will have INVENTORY attribute
# instantiate an instance of VENDOR we can optionally pass in a list for INVENTORY--> inventory=[]

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

# every instance of vendor has ADD instance method
# ADDs one item to inventory
# returns the item that was added

    def add(self, item):
        self.inventory.append(item)
        return item

# every instance of vendor has REMOVE instance method
# REMOVEs one item from inventory
# this method removes the "matching" item from inventory
# returns the item that was removed

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

# IF no matching items in INVENTORY, return False

#loop through each item in the inventory 
#take out the category associated with that item 
#return a list with the items in that category 

    def get_by_category(self, category=""):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, friend, my_item, their_item):


        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
        # if their_item in friend.inventory:
            # friend.inventory.remove(their_item)
            # self.inventory.append(their_item)
        # else:
        #     return False

#WAVE 3 PSEUDOCODE
#step 1: stringify intance Item
#step 2: in the Vendor file, create instance method "swap_items(self, friend_vendor, my_item, their_item)"
    #logic: loop through items in inventory and remove my_item from inventory and append's to friends_inventory(initiate an empty list or is this in friend_vendor?)
            #loop through friends_inventory and remove their_item from friends_inventory and add to inventory
            #return True
            #if this vendor's inventory doesnt contain my_item or friends_inventory doesnt contain "their_item"
            # return false