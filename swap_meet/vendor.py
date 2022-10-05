class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
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
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        else:
            self.add(friend.inventory[0])
            friend.add(self.inventory[0])
            self.remove(self.inventory[0])
            friend.remove(friend.inventory[0])
            return True

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        ratings = []
        if items == []:
            return None

        for item in items:
            ratings.append(item.condition)

        best = max(ratings)
        best_list = []
        for item in items:
            if item.condition == best:
                best_list.append(item)
        return best_list[0]
