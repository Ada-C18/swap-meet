from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
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
       #return a list of "items" in the inventory with that category
        list_of_items = []
        for item in self.inventory:
            if category ==item.category:
                list_of_items.append(item)
                
        return list_of_items
        
    def swap_items(self,friends_vendor, my_item,their_item):
        if my_item not in self.inventory or their_item not in friends_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        friends_vendor.inventory.append(my_item)
        friends_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
        
        