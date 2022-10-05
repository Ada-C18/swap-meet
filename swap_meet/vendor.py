class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self,category):
        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        my_index = self.inventory.index(my_item)
        friend_index = friend.inventory.index(their_item)

        my_removed_item = self.inventory.pop(my_index)
        friend_removed_item = friend.inventory.pop(friend_index)

        friend.inventory.append(my_removed_item)
        self.inventory.append(friend_removed_item)
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        
        my_item = self.inventory.pop(0)
        friend_item = friend.inventory.pop(0)

        friend.inventory.append(my_item)
        self.inventory.append(friend_item)

        return True