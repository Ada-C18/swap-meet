from swap_meet import item


class Vendor:
    # init attributes: inventory(list)
    def __init__(self, inventory =  []):
        self.inventory = inventory

    # method to add items to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
        
    # method to remove items from inventory
    def remove(self, item):
        try:
            self.inventory.remove(item)
        except(ValueError):
            return False

        return item
   
    # iterates through inventory and puts into seperate list based on category attribute
    def get_by_category(self, category):
        filter = []
        for item in self.inventory:
            if item.category == category:
                filter.append(item)

        return filter 

    def swap_items(self, other_vendor, item_a, item_b):
        
        try:
            index_1 = self.inventory.index(item_a)
            index_2 = other_vendor.inventory.index(item_b)
        except(ValueError):
            return False 
        
        self.inventory.append(other_vendor.inventory.pop(index_2))
        other_vendor.inventory.append(self.inventory.pop(index_1))
        return True

        # if item_a in self.inventory and item_b in other_vendor.inventory:
        
        #     self.inventory.remove(item_a)
        #     self.inventory.append(item_b)

        #     other_vendor.inventory.remove(item_b)
        #     other_vendor.inventory.append(item_a)
        #     return True
        # else:
        #     return False 