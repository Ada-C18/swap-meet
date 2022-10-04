from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item
    
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        
        self.inventory.remove(remove_item)
        return remove_item
    
    def get_by_category(self, item_category):
        items_list = [item for item in self.inventory if item.category == item_category]

        return items_list
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        friend.add(self.remove(my_item))
        self.add(friend.remove(their_item))
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        return self.swap_items(friend, self.inventory[0], friend.inventory[0])