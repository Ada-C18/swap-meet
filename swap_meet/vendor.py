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
    
    def __str__(self):
        self.inventory[0] = "My first item"
    
    def swap_first_item(self, friend):

        if len (self.inventory) ==0 or len (friend.inventory) ==0:
            return False
        

        friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(friend.inventory[0])
        friend.remove(friend.inventory[0])
        
        
        return True
