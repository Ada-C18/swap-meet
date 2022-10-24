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
            if item.category == category:
                merch.append(item)
        return merch

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True

        return False

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            self.swap_items(friend, my_item=self.inventory[0], their_item=friend.inventory[0])
            return True
        # access self.inventory[0] and friend.inventory[0]
        # remove my item from self.inventory and add it to friend.inventory
        # remove item from friend.inventory and add it to self.inventory

    def get_best_by_category(self, category):
        best_item = None
        for item in self.get_by_category(category):
            if best_item is None:
                best_item = item
            elif item.condition > best_item.condition:
                best_item = item
        return best_item

    # this function will swap with other, get my priority, get their priority
    # def swap_best_by_category(self, other, my_priority, their_priority):
    # can use get_best_by_category and swap_first_item (since it's the best by category)

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if their_best_item is None or my_best_item is None:
            return False
        else:
            self.swap_items(other, my_best_item, their_best_item)
            return True