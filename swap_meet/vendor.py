
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

#WAVE 3 PSEUDOCODE
#step 1: stringify intance Item
#step 2: in the Vendor file, create instance method "swap_items(self, friend_vendor, my_item, their_item)"
    #logic: loop through items in inventory and remove my_item from inventory and append's to friends_inventory(initiate an empty list or is this in friend_vendor?)
            #loop through friends_inventory and remove their_item from friends_inventory and add to inventory
            #return True
            #if this vendor's inventory doesnt contain my_item or friends_inventory doesnt contain "their_item"
            # return false

#WAVE 4 PSEUDOCODE
#create instance method swap_first_item(self, friend)
    #logic:
    # check to make sure self inventory and friend inventory is not empty? 
    # loop through the self.inventory to get first item
            # remove it and then add it to the friends friends inventory[0]
            #if self or friend have an empty inventory return false

    def swap_first_item(self, friend):
        if len(self.inventory) < 1 or len(friend.inventory) < 1:
            return False
        else:
            first_item = self.inventory.pop(0)
            other_first_item = friend.inventory.pop(0)

            self.remove(first_item)
            friend.add(first_item)
            friend.remove(other_first_item)
            self.add(other_first_item)
            return True

            for item in self.inventory:
                self.inventory.remove(item[0])
                friend.inventory[0].add(item[0])
            for f_item in friend.inventory:
                friend.inventory.remove(f_item[0])
                self.inventory[0].add(f_item[0])
                return True
