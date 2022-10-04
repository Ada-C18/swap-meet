class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            self.inventory.remove(my_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if len(self.inventory) > 0 and len(friend.inventory) > 0:
            friend.inventory.append(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            self.inventory.remove(self.inventory[0])
            return True
        else:
            return False
