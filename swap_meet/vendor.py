#from swap_meet.item import Item

class Vendor:
    # def __init__(self, inventory = []):
    # default value None is IMMUTABLE. MUTABLE type should not be used in DEFAULT argument.

# Wave 1    
    def __init__(self, inventory = None):    
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, add_item):
        '''
        Returns the item that was added
        '''
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        '''
        Returns the item that was removed
        '''
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False

# Wave 2
    def get_by_category(self, category_str):
        '''
        Returns a list of Strings (items) in the inventory with given category.
        '''
        same_category_list = []
        for item in self.inventory:
            # does not need import at this point
            # cause of "dynamic type" does not care about ".category" until it sees Item class
            # varies in different languages
            if item.category == category_str:
                same_category_list.append(item)
        return same_category_list
         

# Wave 3
    def swap_items(self, swap_vendor, my_item, their_item): 
        '''
        Returns True if swap items action is successful.
        Otherwise, returns False.
        '''
        if their_item in swap_vendor.inventory and my_item in self.inventory:
            # Mistake made; using swap_vendor.inventory
            # Class methods must be called on a class objects, not a list 
            swap_vendor.remove(their_item)
            self.add(their_item)
            self.remove(my_item)
            swap_vendor.add(my_item)
            return True
        # okay to delete, clear to leave it?
        return False 


# Wave 4      
    def swap_first_item(self, swap_vendor):
        '''
        Returns True if swap first avaiable item action is successful.
        Otherwise, returns False.
        '''
        if len(self.inventory) >= 1 and len(swap_vendor.inventory) >= 1:
            return self.swap_items(swap_vendor, self.inventory[0], swap_vendor.inventory[0])


# Wave 6
    def get_best_by_category(self, given_category):
        '''
        Returns the item with the best condition in a certain category.
        '''
        items = self.get_by_category(given_category)
        if len(items) > 0:
            best_item = max(items, key=lambda i:i.condition)
            return best_item
        return None         

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Returns True if swap the best item (category) action is successful.
        Otherwise, returns False.
        '''
        # watch out for self.func or other.func
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item is not None and their_best_item is not None:           
            self.swap_items(other, my_best_item, their_best_item)
            return True