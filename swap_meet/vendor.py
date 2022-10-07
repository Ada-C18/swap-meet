from swap_meet.item import Item
#wave1
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
    def swap_items(self, friend_vendor, my_item, their_item): 

        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.inventory.append(my_item)

            friend_vendor.remove(their_item)
            return True
        else:
            return False

#wave 4:
    def swap_first_item(self, swap_vendor):

        if len(self.inventory) == 0 or len(swap_vendor.inventory) == 0:
            return False
        swaping = self.swap_items(swap_vendor,self.inventory[0],swap_vendor.inventory[0])
        return swaping


# wave 6:
    def get_best_by_category(self, category):   
        best_item = None
        best_condition = 0 
        for item in self.get_by_category(category):
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):  
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item  = other.get_best_by_category(my_priority)
        if my_best_item is None or their_best_item is None:
            return False
        return self.swap_items(other, my_best_item, their_best_item)




