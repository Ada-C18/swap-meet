from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return self.item

    
    def get_by_category(self, category):
        # return [item for item in self.inventory if item.category == category]
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        self.friend = friend
        self.my_item = my_item
        self.their_item = their_item
        
        if self.their_item not in friend.inventory:
            return False
        
        if self.my_item not in self.inventory:
            return False
        
        if self.my_item:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
        
        if self.their_item:
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        



#   - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
#   - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
#   - It returns `True`
#   - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`
