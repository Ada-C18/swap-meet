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
        if not self.inventory or not friend_vendor.inventory:
            return False        
        if self.inventory and friend_vendor.inventory:
            self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True

# Wave 6
#========================================= 
    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        if not items_by_category:
            return None        
        
        best_item = items_by_category[0]
        best_condition = 0
        for item in items_by_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
        # need to import something else for this line below to work
        #best_condition = max(items_by_category, key= item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        else:
            self.swap_items(other, my_best_item, their_best_item)
            return True

