class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

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

        friend.inventory.append(self.remove(my_item))
        self.inventory.append(friend.remove(their_item))
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        
        my_item = self.inventory.pop(0)
        friend_item = friend.inventory.pop(0)

        friend.inventory.append(my_item)
        self.inventory.append(friend_item)

        return True

    def get_best_by_category(self, category):
        best_item_condition = -1
        best_item = None
        for item in self.inventory:
            if item.category == category and item.condition > best_item_condition:
                best_item_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        other_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        if not other_item or not my_item:
            return False

        return self.swap_items(other, my_item, other_item)