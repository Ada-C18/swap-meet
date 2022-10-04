from pickle import FALSE
from swap_meet.item import Item

class Vendor(Item):
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add_item(self, item):
        self.inventory.append(item)
        return item

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category_name):
        list_item = []
        for item in self.inventory:
            if category_name == item.category:
                list_item.append(item)
        return list_item

# friend_vendor = Vendor()
# my_vendor = Vendor()
# their_item = Item()
# my_item = Item()

# friend_vendor.get_by_category(friend_inventory)
# my_vendor.get_by_category(my_inventory)

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in my_item.inventory and their_item in friend_vendor.inventory:
            self.remove_item(my_item)
            friend_vendor.add_item(my_item)
            self.add_item(their_item)
            friend_vendor.remove_item(their_item)
        return False

    def swap_first_item(self, friend_vendor):
        if len(friend_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
        first_inventory = self.inventory[0]
        friend_first = friend_vendor.inventory[0]
        self.remove_item(first_inventory)
        friend_vendor.add_item(first_inventory)
        self.add_item(friend_first)
        friend_vendor.remove_item(friend_first)
        return True

    def get_best_by_category(self, friend_vendor, my_item, their_item):
        

