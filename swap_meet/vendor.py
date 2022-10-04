from swap_meet.item import Item

# Wave 1
#======================================================
class Vendor:
    #optionally pass in argument "inventory"
    def __init__(self, inventory = None):
        # if "inventory" arugment is passed in, use that
        if inventory:
            self.inventory = inventory
        # otherwise, if there's no inventory argument, initialize an empty list
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False

# Wave 2
#======================================================
# need to import from Item for this method to work
    def get_by_category(self, category):
        inventory_categories = []
        for item in self.inventory:
            if item.category == category:
                inventory_categories.append(item)
        return inventory_categories

# Wave 3
#======================================================
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.remove(my_item)
            friend_vendor.add(my_item)
            friend_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

# Wave 4
#======================================================
    def swap_first_item(self, friend_vendor):
        # need try and except otherwise if the inventory list is empty
        # the code won't work
        try:
            self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True
        except: 
            if not self.inventory or not friend_vendor.inventory:
                return False

        # if self.inventory and friend_vendor.inventory:
        #     self.remove(self.inventory[0])
        #     friend_vendor.add(self.inventory[0])
        #     friend_vendor.remove(friend_vendor.inventory[0])
        #     self.add(friend_vendor.inventory[0])
        #     return True
        # if not self.inventory or not friend_vendor.inventory:
        #     return False

