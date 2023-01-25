class Vendor:
    def __init__(self, inventory= None):
        self.inventory = inventory if inventory else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)

        return item
    
    def get_by_category(self, category):
        items_in_category = [item for item in self.inventory 
                            if item.category == category]
        return items_in_category 

    """def find_index(self, item_to_find):
        i = 0
        for item in self.inventory:
            if item == item_to_find:
                item_index = i
            i += 1
        
        return item_index"""
    
    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        my_item_index = self.inventory.index(my_item)
        their_item_index = other.inventory.index(their_item)

        self.inventory[my_item_index] = their_item
        other.inventory[their_item_index] = my_item

        return True
    
    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other.inventory[0]

        return self.swap_items(other, my_first_item, their_first_item)
    
    def get_best_by_category(self, category):
        if not self.inventory:
            return False
        
        best_item_by_cat = self.inventory[0]
        category_not_in_inventory = True

        for item in self.inventory:
            if item.category == category:
                category_not_in_inventory = False
                if item.condition >= best_item_by_cat.condition:
                    best_item_by_cat = item
        # try:
        # return max(self.get_by_category(category), key= lambda item: item.condition)
        # except ValueError:
        # return None
        if category_not_in_inventory:
            return None

        return best_item_by_cat
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, their_best_item)
