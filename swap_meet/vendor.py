class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or list()
        
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        my_result = self.remove(my_item)
        their_result = vendor_friend.remove(their_item)
        self.add(their_item)
        vendor_friend.add(my_item)
        return True
        
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = friend.inventory[0]
        return self.swap_items(friend, my_first_item, friend_first_item)
    
    def get_best_by_category(self, category):
        return max(self.get_by_category(category), key=lambda item: item.condition, default=None)
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if not my_item or not their_item:
            return False
        return self.swap_items(other, my_item, their_item)