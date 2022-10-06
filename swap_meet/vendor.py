from .item import Item

class Vendor:
    
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
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
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.remove(my_item)
        other.add(my_item)
        other.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        
        friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(friend.inventory[0])
        friend.remove(friend.inventory[0])
        return True

        # if self.inventory and friend.inventory:
        #     return self.swap_items(friend, self.inventory[0], friend.inventory[0])
        # return False
    
    def get_best_by_category(self, category):
        get_category = self.get_by_category(category)
        if get_category == []:
            return None
        best_condition = get_category[0]
        for item in get_category:
            if item.condition > best_condition.condition:
                best_condition = item
        return best_condition

    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if their_best_item == None or best_item == None:
            return False
        else:
            self.swap_items(other, best_item, their_best_item)
            return True
    
    def get_best_by_age(self):
        if self.inventory == []:
            return None
        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other):
        newest_item = self.get_best_by_age()
        their_newest_item = other.get_best_by_age()
        if newest_item == None or their_newest_item == None:
            return False
        else:
            self.swap_items(other, newest_item, their_newest_item)
            return True

