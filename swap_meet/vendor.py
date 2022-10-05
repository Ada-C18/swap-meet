class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
    
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item) 
            self.add(their_item)
            self.remove(my_item)
            friend.remove(their_item)
            
            return True
        else:
            return False
    
    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        else:
            return False
        
    def get_best_by_category (self, category):
        best_item = None
        best_condition = 0
        
        for item in self.inventory:
            if item.category == category and item.condition > best_condition:
                best_item = item
                best_condition = item.condition
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = self.get_best_by_category(my_priority)
        
        return self.swap_items(other, my_best, their_best)
        
    
    
            
            
