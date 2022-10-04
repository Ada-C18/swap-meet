class Vendor:
    
    def __init__(self, inventory=[]):
        # we can also do none or false using if else
        self.inventory = inventory 
    def add(self,item):
        self.inventory.append(item)
        return item
    def remove(self,item):
        for inventory_item in self.inventory:
            if inventory_item==item:
                self.inventory.remove(item)
                return item
        return False
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.inventory.remove(my_item)
            friend_vendor.inventory.append(my_item)
            friend_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False




