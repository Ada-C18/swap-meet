from .item import Item

class Vendor():
    #constractor
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    # adding an item to the list of inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # removing an item from the inventory list
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    # returning a list of items when giving a spicific category
    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)

        return items_list
    
    # swap items between to list's
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory :
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        return False

    # swaping the first item between two inventories
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory :
            return False
        self.swap_items(friend, self.inventory[0],friend.inventory[0])
        return True

    # returning the best item in an inventory when given a spicific category
    def get_best_by_category(self, category):
        max_condition = 0
        max_item = None
        items_list = self.get_by_category(category)
        for item in items_list:
            if item.condition > max_condition:
                max_condition = item.condition
                max_item = item
        return max_item
    
    # swaping the best item given a spicific category between two inventories 
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if not my_item or not their_item:
            return False
        return self.swap_items(other, my_item, their_item)



