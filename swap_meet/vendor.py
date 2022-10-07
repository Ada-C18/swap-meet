class Vendor:
    
    def __init__(self,inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):

        return [item for item in self.inventory if category == item.category]

    def swap_items(self,friend, my_item, their_item):

        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            friend.inventory.append(my_item)
            return True
        return False
    
    def swap_first_item(self, friend):

        if self.inventory and friend.inventory:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    def get_best_by_category(self, category):

        categories = self.get_by_category(category)

        if not categories:
            return None
        return max(categories, key = lambda x : x.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        other_vendor = other.get_best_by_category(my_priority)
        my_vendor = self.get_best_by_category(their_priority)

        return self.swap_items(other, my_vendor, other_vendor)

    def swap_by_newest(self, other, their_newest, my_newest):

        return self.swap_items(other, min(self.inventory, key = lambda x : x.age) , min(other.inventory, key = lambda x : x.age))





