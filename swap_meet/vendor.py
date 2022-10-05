# relative import
# from .item import Item

# full import
from unicodedata import category
from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        # inventory is an empty list by default
        # we can optionally pass in a list with the keyword argument inventory
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''
        Input: item
        Ouput: item that was removed, or False if no matching item in list
        Method removes the matching item from the inventory
        '''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, input_category):
        ''' 
        Input: a string, representing a category
        Output: returns a list of Items in the inventory with that category
        '''
        category_items = []

        for item in self.inventory:
            if item.category == input_category:
                category_items.append(item)
        return category_items

    # wave 3 - write method swap_items
    def swap_items(self, friend_vendor, my_item, their_item):
        '''
        Input: instance of Vendor (friend_vendor), instance of Item (my_item), instance of Item (their_item)
        Output: 
        - True, if my_item in inventory and their_item in their inventory
        -- inventories updated (their_item in my inventory, my_item in their inventory)
        - False, if my_item not in inventory or their_item not in their inventory
        '''

        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        else:
            self.add(their_item)
            self.remove(my_item)

            friend_vendor.add(my_item)
            friend_vendor.remove(their_item)
            return True

    def swap_first_item(self, friend_vendor):
        ''''
        Input: instance of another Vendor (friend_vendor)
        Output: 
        True (and swaps first item in both inventories)
        False if self.inventory or friend_vendor.inventory are empty
        '''
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False

        self.swap_items(
            friend_vendor, self.inventory[0], friend_vendor.inventory[0])
        return True

    def get_best_by_category(self, given_category):
        '''
        Method looks through the instance inventory for the item with the highest condition and matching category

        Input: category string
        Output:
        Return item, if item category in inventory (return 1 item if 2+ items with same best condition)
        Return None, if no items in the inventory that match the category
        '''
        # if item not in self.get_by_category(category):
        #     return None

        # self.get_by_category gets items with category in parameter
        for item in self.get_by_category(given_category):
            # Find item with the best condition in a specified category
            best_item = ""
            highest_condition = 0

            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
            # if item.condition == highest_condition:
            #     best_items.append(item)
            return best_item


# 2. `swap_best_by_category` - swap the best item of certain categories with another `Vendor`
#     1. can use `swap_items` here
#     2. return `True` → if their_priority in my inventory, swap their_priority with my_priority
#     3. return `False` → if their_priority not in Vendor/my inventory OR my_priority not in their `other`/inventory

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: instance of Vendor(other), my_priority(category str), their_priority(category str)
        Output:
        `True` → if their_priority in Vendor inventory, swap their_priority with my_priority
        `False` → if their_priority not in Vendor inventory OR my_priority not in `other`
        '''
        pass
