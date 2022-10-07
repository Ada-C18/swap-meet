class Vendor:
    MAX_AGE = 1000
# Wave 1    
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory 
    def add(self,item):
        self.inventory.append(item)
        return item
    def remove(self,item):
        for inventory_item in self.inventory:
            if inventory_item == item:
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

        self.remove(my_item)
        friend_vendor.add(my_item)
        friend_vendor.remove(their_item)
        self.add(their_item)
        return True
        

# Wave 4
    def swap_first_item(self, friend_vendor):
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False

        return self.swap_items(friend_vendor, self.inventory[0], 
        friend_vendor.inventory[0])


# Wave 6

    def get_best_by_category(self, category): 
        matching_category_items = self.get_by_category(category)
        highest_condition = 0
        highest_item = None
        for item in matching_category_items:
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_item = item
        return highest_item



    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item == None or their_best_item == None:
            return False
        return self.swap_items(other, my_best_item, their_best_item)


# Optional Enhancement
    def find_newest_item (self):
        min_item_age = self.MAX_AGE
        min_item = None
        for item in self.inventory:
            if item.age < min_item_age:
                min_item_age = item.age
                min_item = item
        return min_item

    def swap_by_newest(self, friend_vendor):
        vendor_newest_item = self.find_newest_item()
        friend_newest_item = friend_vendor.find_newest_item()
        return self.swap_items(friend_vendor, vendor_newest_item, friend_newest_item)






                
                    



        




