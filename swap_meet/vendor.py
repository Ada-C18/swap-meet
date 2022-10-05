

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

#WAVE 3 PSEUDOCODE ============================================================
#step 1: stringify intance Item——COMPLETED
#step 2: in the Vendor file, create instance method "swap_items(self, friend_vendor, my_item, their_item)"
    #logic: loop through items in inventory and remove my_item from inventory and append's to friends_inventory(initiate an empty list or is this in friend_vendor?)
            #loop through friends_inventory and remove their_item from friends_inventory and add to inventory
            #return True
            #if this vendor's inventory doesnt contain my_item or friends_inventory doesnt contain "their_item"
            # return false

    # WAVE 3 SOLUTION USING REMOVE AND APPEND METHODS -->
    # def swap_items(self, friend, my_item, their_item):
    #     if my_item in self.inventory and their_item in friend.inventory:
    #         self.inventory.remove(my_item)
    #         friend.inventory.append(my_item)
    #         friend.inventory.remove(their_item)
    #         self.inventory.append(their_item)
    #         return True
    #     else:
    #         return False
    
    # REUSING THE METHODS ADD AND REMOVE WE CREATED EARLIER -->
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False


# WAVE 4 PSUEDO CODE===========================================================
# write method = SWAP_FIRST_ITEM()
# instances of vendor have instance method named SWAP_FIRST_ITEM()

# it takes one argument = other_vendor
    def swap_first_item(self, other_vendor):
# if itself or other_vendor have empty inventory...
# return FALSE
        if len(self.inventory) < 1 or len(other_vendor.inventory) < 1:
            return False
        else:
# considers:  1st item in inventory AND first item in other_vendor's inventory            
# self removes 1st item in inventory AND adds to other_vendor's inventory
# it return true
            first_item = self.inventory.pop(0)
            other_first_item = other_vendor.inventory.pop(0)

            self.remove(first_item)
            other_vendor.add(first_item)
            self.add(other_first_item)
            other_vendor.remove(other_first_item)
        return True


# WAVE 5 PSUEDO CODE ==========================================================
# we will create THREE ADDITIONAL MODULES
# we will create THREE ADDITIONAL CLASSES


# CLASS 1— CLOTHING
# has 1 attribute = CATEGORY
# it's stringify method returns = "The finest clothing you could wear."


# CLASS 2 — DECORE
# has 1 attribute = CATEGORY
# it's stringify method returns = "Something to decorate your space."


# CLASS 3 — ELECTRONICS
# has 1 attribute = CATEGORY
# it's stringify method returns = "A gadget full of buttons and secrets."


# ALL 3 CLASSES and ITEM CLASS have attribute called CONDITION
# CONDITION can be optionally provided in the initializer, default=0

# ALL 3 CLASSES and ITEM CLASS have instance method named CONDITION_DESCRIPTION
        # should describe the condition IN WORDS based on the VALUE = range 0-5
        # feel free to have fun with condition descriptions
        # the condition_description method behaves the same for all three classes

#WAVE 6 
    def get_best_by_category(self, category):
        list_of_items = self.get_by_category(category)
        best_item = self.find_max_item(list_of_items) 
        return best_item  

    def find_max_item(self, items):
        if len(items) == 0:
            return None
        best_item = items[0] 
        for item in items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
            #swap my_best_item with their_best_item
            my_best_item = self.get_best_by_category(their_priority)
            their_best_item = other.get_best_by_category(my_priority)
            return self.swap_items(other, my_best_item, their_best_item)
            
# WAVE 6 ======================================================================
# write TWO METHODS

# FIRST METHOD TO CREATE
# VENDORs have method get_best_by_category 
# take 1 argument: CATEGORY, as a string
# looks through INVENTORY for the item with highest CONDITION and matching CATEGORY
# RETURNs this item
# if no items in INVENTORY that match, RETURN None
# if 1 item in INVENTORY that match, RETURN 1 item only

    def get_best_by_category(self, category=""):

        if len(self.get_by_category(category)) == 0:
            return None
        best_item = (max(self.get_by_category(category), key=lambda x:x.condition))
        return best_item

# SECOND METHOD TO CREATE
# takes in 3 arguments
        # OTHER = VENDOR instance to trade with
        # MY_PRIORITY = CATEGORY that VENDOR wants to receive
        # THEIR_PRIORITY = CATEGORY that OTHER wants to recieve

# best item that matches THEIR_PRIORITY is swapped
# best item that matches MY_PRIORITY is swapped

# it returns True
# if VENDOR has no item that matches THEIR_PRIORITY, returns False
# if OTHER has no item that matches THEIR_PRIORITY, returns False
    # def swap_best_by_category(self, other, my_priority, their_priority):
        
        swap_items = self.swap_items(other, my_priority, their_priority)

        if swap_items == False:
            return False
        return True
    
    
