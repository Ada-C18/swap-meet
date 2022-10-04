class Vendor:
    def __init__(self, inventory = None):
        
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
            
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item:
            return False
        elif item not in self.inventory:
            return False    
        
        self.inventory.remove(item)
        return item
        
    def get_by_category(self, category):
        new_list = []
        
        for item in self.inventory:
            if category == item.category:
                new_list.append(item)
        return new_list
    
# ***** added for wave_03 *****
    def swap_items(self, Vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in Vendor.inventory:
            # removes item from self inventory and adds it to friend's inventory
            self.inventory.remove(my_item)
            Vendor.inventory.append(my_item)
            
            # removes item from friend's inventory and adds it to self inventory
            Vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            
            return True
        
        else:
            return False
        
# ***** added for wave_04 *****
    def swap_first_item(self, Vendor):
        if not self.inventory or not Vendor.inventory:
            return False
        # grabs first items from inventory's
        self_first_item = self.inventory[0]
        vendor_first_item = Vendor.inventory[0]

        #removes first items from inventory's
        del self.inventory[0]
        del Vendor.inventory[0]

        # swaps first items and adds to beginning of inventory
        self.inventory.insert(0, vendor_first_item)
        Vendor.inventory.insert(0, self_first_item)

        return True