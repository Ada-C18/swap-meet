from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
    # inventory is an empty list
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.item = item           # item (this method takes only 1 item)
        self.inventory.append(item)
        return item

    def remove(self, item): 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
# wave 2
    def get_by_category(self, category):
        items_inventory = []
        for item in self.inventory:
            if item.category == category:
                items_inventory.append(item)
        return items_inventory
        
# wave 3

    def swap_items(self, friend_vendor, my_item, their_item):  #attributes can be instances of classes? 
        self.friend_vendor = friend_vendor
        self.my_item = my_item
        self.their_item = their_item
        #remove my item and add it to friend_vendor inventory: 
        # remove their_item from friend_vendor inventory and add it to my inventory
        # if no item in inventory return False
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.inventory.append(my_item)

            friend_vendor.remove(their_item)
            return True
        else:
            return False

    # friend_vendor = Vendor()
    # my_item = Item()
    # their_item = Item()
