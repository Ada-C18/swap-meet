from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory
        
# default list error here (inventory= None)

    def add(self, item):
        self.inventory.append(item)
        return item 
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        self.inventory.append(category)
        return self.inventory 
        
    def get_by_category(self, category):
        list_of_category_match = []
        for i in self.inventory:
            if i.category == category:
                list_of_category_match.append(i)
        return list_of_category_match
        
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
            
        friend.add(my_item)
        self.remove(my_item)
        
        friend.remove(their_item)
        self.add(their_item)
        
        return True
  