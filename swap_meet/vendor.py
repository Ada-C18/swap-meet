class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory != None else []
      
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

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in another_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        items_cat = self.get_by_category(category)
        if items_cat == []:
            return None
        best_item = max(items_cat, key = lambda i: i.condition)
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if not their_item or not my_item:
            return False
        self.swap_items(other, my_item, their_item)
        return True
        
    def swap_first_item(self, friend):
        if friend.inventory == [] or self.inventory == []:
            return False
        else:
            friend_item = friend.inventory[0]
            our_item = self.inventory[0]
            self.swap_items(friend, our_item, friend_item)
            return True
    
    def swap_by_newest(self, other):
        if other.inventory == [] or self.inventory == []:
            return False
        else:
            other_item = min(other.inventory, key = lambda i: i.age)
            our_item = min(self.inventory, key = lambda i: i.age)
            self.swap_items(other, our_item, other_item)
            return True