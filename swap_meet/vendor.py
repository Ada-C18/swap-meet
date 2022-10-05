class Vendor:
    def __init__(self, inventory = None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory 
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        else:
            return False 

    def get_by_category(self,category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        
        return items_list 
    
    def swap_items(self, friend, my_item, friend_item):
        if my_item not in self.inventory or friend_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(friend_item)
        self.add(friend_item)

        return True 
    
    def swap_first_item(self, friend):
        if len (self.inventory) == 0 or len (friend.inventory) == 0:
            return False
        friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(friend.inventory[0])
        friend.remove(friend.inventory[0])
        
        return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None

        return max(category_list, key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if their_best and my_best:
            self.swap_items(other, my_best, their_best)
            return True
        else:
            return False
    

