class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
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
        item_list =[item for item in self.inventory if item.category == category]
        return item_list

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.add(their_item)
        other.add(my_item)
        self.remove(my_item)
        other.remove(their_item)
        return True

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
            friend.inventory.append(our_item)
            self.inventory.append(friend_item)
            friend.inventory.pop(0)
            self.inventory.pop(0)
            return True
