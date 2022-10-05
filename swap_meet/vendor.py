from tokenize import String
from types import MemberDescriptorType
from swap_meet.item import Item

#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):

        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):                         
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if category == item.category]
        # items_list = []
        # for item in self.inventory:
        #     if category == item.category:
        #         items_list.append(item)
        # return items_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        self.add(their_item)
        friend.add(my_item)
        self.remove(my_item)
        friend.remove(their_item)

        return True

    #Takes in an instance of another vendor and trades first item from self and vendor list
    def swap_first_item(self, friend):

    #return false if either list does not have item
        if not self.inventory or not friend.inventory:
            return False
    
    #variables to access inventory list index 0
        self_new_inventory = self.inventory[0]
        friend_new_inventory = friend.inventory[0]

    #remove index 0 from each list (friends and self) and swap each item 
        self.remove(self_new_inventory)
        friend.remove(friend_new_inventory)
        self.add(friend_new_inventory)
        friend.add(self_new_inventory)
        return True

        
#wave 6
# Get the item with the best condition in a certain category
    def get_best_by_category(self, category):
        #assign variable best_category to get_by_category above to invoke
        best_category = self.get_by_category(category)
     
        # best_category = []
        # #loop through self in inventory, if category is == item.category, append 
        # for item in self.inventory:
        #     if category == item.category:

        # If there are no items in the `inventory` that match the category return `None
        if not best_category:
            return None 
      
        #variable to compare
        best_condition = best_category[0]

        # Loop through the instance's `inventory` for the item with the highest condition and associated category
        for item in best_category:
            if item.condition > best_condition.condition:
                best_condition = item

        # Return item
        return best_condition 

    def swap_best_by_category(self, other, my_priority, their_priority):
#The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
#It returns `True`
#If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
#If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
        pass