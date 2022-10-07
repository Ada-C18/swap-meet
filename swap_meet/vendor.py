from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
               

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)    
            return item


    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        else:
            self.remove(my_item) 
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            return self.add(their_item)
            


    def swap_first_item(self, another_vendor):
        if self.inventory == [] or another_vendor.inventory == []:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = another_vendor.inventory[0]
            return self.swap_items(another_vendor, my_first_item, their_first_item)



    def get_best_by_category(self, category):
        
        items_in_category = self.get_by_category(category)

        if items_in_category == False:
            return None
        else: 
            best_item_so_far = None
            for item in items_in_category: 
                if best_item_so_far is None or best_item_so_far.condition < item.condition: 
                    best_item_so_far = item
            return best_item_so_far


    def swap_best_by_category(self, other, my_priority, their_priority):
        # my_priority= category vendor wants to receive 
        # their_priority=category other wants to receive
       
        my_best_item_in_category =self.get_best_by_category(their_priority)  
        their_best_item_in_category = other.get_best_by_category(my_priority)
        if my_best_item_in_category is None or their_best_item_in_category is None:
            return False
        return self.swap_items(other,my_best_item_in_category,their_best_item_in_category)
        






    
