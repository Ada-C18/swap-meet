from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=[]): # to set initial attributes
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

    def get_by_category(self, category):
        merch =[]
        for item in self.inventory:
            if item.category is category:
                merch.append(item)
        return merch

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True

        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.remove(self.inventory[0])
            friend.add(friend.inventory)
            friend.remove(friend.inventory[0])
            self.add(self.inventory)
        else:
            if len(self.inventory) == 0 or len(friend.inventory) == 0:
                return False
        return True