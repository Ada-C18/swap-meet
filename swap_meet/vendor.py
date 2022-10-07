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
        return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        first_item = self.inventory[0]
        first_item_vendor = other_vendor.inventory[0]
        self.swap_items(other_vendor, first_item,first_item_vendor)
        
        return True
    
    def get_best_by_category(self, category):
        #items_in_category is a list of items 
        all_items_in_category = self.get_by_category(category)
        if all_items_in_category == []:
            return None
        best_item = all_items_in_category[0]
        #inventory is list of items. we should check if highest_condition and Matching_category item are in the Item list
        #if no items matching the category
        for item in all_items_in_category:
            if item.condition > best_item.condition:
                best_item = item
            
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
    
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item == None or their_best_item == None:
            return False
        self.swap_items(other,my_best_item, their_best_item)
            
        return True



        

    

    
        

    
        
    
    
    




        
