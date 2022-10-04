#from swap_meet.item import Item

class Vendor:
    # def __init__(self, inventory = []):
    # By having MUTABLE TYPE in DEFAULT argument, HAVE PROBLEMS in INTERGRATION TEST ISSUE
    # default value none is immutable. mutable xx
    # self.inventory : list of Strings, multiple items; Vendor(inventory=[item_a, item_b, item_c]

# Wave 1    
    def __init__(self, inventory = None):    
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

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
        # a string with the keyword argument category
        # return list of items in that category
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
        if their_item in swap_vendor.inventory and my_item in self.inventory:
            # Mistake made; using swap_vendor.inventory
            # Class methods must be called on a class objects, not a list 
            swap_vendor.remove(their_item)
            self.add(their_item)
            self.remove(my_item)
            swap_vendor.add(my_item)
            return True
        #- okay to delete?
        return False 

# Wave 4
    def swap_first_item(self, swap_vendor):
        if len(self.inventory) >= 1 and len(swap_vendor.inventory) >= 1:
            return self.swap_items(swap_vendor, self.inventory[0], swap_vendor.inventory[0])
         
        




