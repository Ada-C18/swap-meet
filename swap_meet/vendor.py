class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        friend.inventory.append(my_item)
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        self.inventory.remove(my_item)
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        # my_item = self.inventory[0]
        # their_item = friend.inventory[0]

        friend.inventory.append(self.inventory.pop(0))
        self.inventory.append(friend.inventory.pop(0))
        return True

