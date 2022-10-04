class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            self.inventory.append(friend.inventory[0])
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            friend.inventory.remove(friend.inventory[0])
        return True
        
