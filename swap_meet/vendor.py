from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if not inventory:
            self.inventory = []
    
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
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            # swaps my_item
            self.inventory.remove(my_item)
            other.inventory.append(my_item)
            # swaps their_item
            self.inventory.append(their_item)
            other.inventory.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other.inventory[0]
            self.swap_items(other, my_first_item, their_first_item)
            return True

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if len(category_items) == 0:
            return None
        best_item = Item()
        for item in category_items:
            if item.condition >= best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        else:
            my_best = self.get_best_by_category(their_priority)
            their_best = other.get_best_by_category(my_priority)
            if not my_best or not their_best:
                return False
            else:
                self.swap_items(other, my_best, their_best)
                return True

    def get_newest(self):
        newest = None
        newest_age = None
        for item in self.inventory:
            if item.age:
                if not newest_age or item.age < newest_age:
                    newest_age = item.age
                    newest = item
        return newest


    def swap_by_newest(self, other):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        else:
            my_newest = self.get_newest()
            other_newest = other.get_newest()
            self.swap_items(other, my_newest, other_newest)
            return True