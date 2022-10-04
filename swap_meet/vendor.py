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
        
