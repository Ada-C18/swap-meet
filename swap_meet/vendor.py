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
        if len (self.inventory) ==0 or len (friend.inventory) ==0:
            return False
        friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(friend.inventory[0])
        friend.remove(friend.inventory[0])
        
        return True
    
    def get_item_condition(self, item): #This can be converted to lambda 
            return item.condition 

    def get_best_by_category(self, category = ""):
        self.category = category 

        category_inventory = self.get_by_category(category)
        if len(category_inventory) == 0:
            return None

        return max(category_inventory, key=self.get_item_condition)
    

    def swap_best_by_category(self,other, my_priority,their_priority):
        self.my_priority = my_priority #My priority category
        self.their_priority = their_priority #Their priority category

        their_list = other.get_by_category(my_priority) #Their things that I want
        my_list = self.get_by_category(their_priority) #My things that they want

        if len (their_list) == 0 or len (my_list) == 0:
            return False
        self.add(max(their_list, key=other.get_item_condition))
        other.remove(max(their_list, key=other.get_item_condition))
        other.add(max(my_list, key=self.get_item_condition))
        self.remove(max(my_list, key=self.get_item_condition))
        
        return True

