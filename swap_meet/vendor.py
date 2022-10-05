from pytest import Item


class Vendor:
    def __init__(self, inventory= None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        items_in_category = [item for item in self.inventory if item.category == category]
        return items_in_category 
    
    def swap_items(self, other, my_item, their_item):
        if not self.inventory or not other.inventory:
            return False
        if (my_item not in self.inventory or their_item not in other.inventory):
            return False

        #TO DO: swap items in their index positions instead of appending
        #self.inventory[my_item] = their_item
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other.inventory.remove(their_item)
        #other.inventory[their_item] = my_item
        other.inventory.append(my_item)
        return True
    
    def swap_first_item(self, other):
        return self.swap_items(other, self.inventory[0], other.inventory[0])
    
    def get_best_by_category(self, category):
        if not self.inventory:
            return False
        
        best_item = self.inventory[0]
        category_not_in_inventory = True

        for item in self.inventory:
            if item.category == category:
                if item.condition > best_item.condition:
                    best_item = item
                category_not_in_inventory = False
        
        if category_not_in_inventory:
            return None

        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, their_best_item)
