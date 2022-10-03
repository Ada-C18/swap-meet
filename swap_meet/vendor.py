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