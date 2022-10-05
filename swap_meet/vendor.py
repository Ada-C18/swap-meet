from .item import Item
class Vendor:
    def __init__(self, inventory= None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
   
    
    def get_by_category(self, category):
        item_by_category = []
        
        for item in self.inventory:
            if category == item.category:
                item_by_category.append(item)
        return item_by_category

    def swap_items(self,another_vender,my_item,their_item):
         if my_item not in self.inventory or their_item not in another_vender.inventory:
            return False
        
         else:
            self.inventory.remove(my_item)
            another_vender.inventory.append(my_item)
            another_vender.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, another_vender):
        
        if not self.inventory or not another_vender.inventory:
            return False
        else:
            return self.swap_items(another_vender, self.inventory[0], another_vender.inventory[0])
        
            
    def get_best_by_category(self, category):
        
        category_list = self.get_by_category(category) 
        if not category_list:
            return None
        return max(category_list, key= lambda item:item.condition)
        

        best_item = category_list[0]
        for item in category_list:
            if item.condiiton > best_item.condition:
                best_item = item
                return best_item

    def swap_best_by_category(self,other,my_priority,their_priority):

        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        else:
            return self.swap_items(other, my_best, their_best)
        
