class Vendor:
# Wave 1    
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

# Wave 2
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

# Wave 3
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False 

        self.inventory.remove(my_item)
        friend_vendor.inventory.append(my_item)
        friend_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
        

# Wave 4
    def swap_first_item(self, friend_vendor):
        if len(self.inventory)==0 or len(friend_vendor.inventory)==0:
            return False
        self_first_inventory = self.inventory[0]
        friend_first_inventory = friend_vendor.inventory[0]
        self.inventory.remove(self_first_inventory)
        friend_vendor.inventory.remove(friend_first_inventory)
        self.inventory.append(friend_first_inventory)
        friend_vendor.inventory.append(self_first_inventory)
        return True
        




