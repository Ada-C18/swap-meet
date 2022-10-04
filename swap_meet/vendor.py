from swap_meet.item import Item

class Vendor:
    # define __init__ class ,takes inventory as a 
    # parameter. Inventory default == None

    # if not inventory initialize an empty list

    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else: 
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item

        except ValueError:
            return False

    def get_by_category(self, category):
        # reminder to ourselves: each item has a category
        # vendor inventory list includes each item as an element

        # need a list
        list_of_items = []

        # we want to check each item to see if its category
        # matches the category passed in as an argument

        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)

        # return list of items that match the category
        return list_of_items

    def swap_items(self, vendor, item_s, item_v):
        
        if item_s not in self.inventory or item_v not in vendor.inventory:
            return False
        # remove item_s from self 
        self.remove(item_s)
        # add item_s to vendor
        vendor.add(item_s)
        # remove item_v from vendor
        vendor.remove(item_v)
        # add item_v to self
        self.add(item_v)
        # return True
        return True
        
