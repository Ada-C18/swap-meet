from swap_meet.item import Item
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor
from swap_meet.clothing import Clothing

class Vendor:
    '''
    object contains an attribute: inventory that is an empty list with an optional parameter
    it also contains the methods: add, remove, get_by_category, swap_items, swap_first_item,
    get_best_by_category
    '''
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        appends item parameter to inventory list
        returns the last item in the inventory list
        '''
        self.inventory.append(item)
        last_inventory_item = self.inventory[-1]

        return last_inventory_item

    def remove(self, item):
        '''
        removes item parameter from inventory
        returns item if item is removed, returns False if nothing is removed
        '''
        for product in self.inventory:
            if product == item:
                self.inventory.remove(item)
                return product
        
        return False

    def get_by_category(self, category):
        '''
        appends items from inventory that match the category parameter
        '''
        item_list = []

        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        
        return item_list

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        swaps items between self and other inventories
        '''
        # Helpers
        self_inventory = self.inventory 
        other_inventory = other_vendor.inventory

        if my_item not in self_inventory or their_item not in other_inventory or other_inventory == [] or self_inventory ==[]:
            return False
        
        for item in self_inventory:
            if item == my_item:
                other_vendor.add(item)
                self.remove(item)

        for item in other_inventory:
            if item == their_item:
                self.add(item)
                other_vendor.remove(item)
        
        return True

    def swap_first_item(self, other_vendor):
        '''
        swaps the first items of self and other inventories
        '''
        # Swap 1st items
        try:
            # Helpers
            self_inventory_item = self.inventory[0]
            other_inventory_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, self_inventory_item, other_inventory_item)

        except:
            return False

    def get_best_by_category(self, category):
        '''
        returns the best condition item by category
        '''
        try:
            condition_check = 0.0
            best_in_category = []

            for item in self.inventory:
                if item.category == category and item.condition > condition_check:
                    condition_check = item.condition
                    best_in_category.clear()
                    best_in_category.append(item)

            return best_in_category[0]
        
        except:
            return None

    def swap_best_by_category(self, other = None, my_priority = None, their_priority = None):
        '''
        takes the best item by category for two vendors and swaps them with each other
        '''
        try:
            # Helpers
            my_best_category = self.get_best_by_category(their_priority)
            their_best_category = other.get_best_by_category(my_priority)

            if len(self.inventory) == 0 or len(other.inventory) == 0 or my_best_category is None or their_best_category is None:
                return False

            self.swap_items(other, my_best_category, their_best_category)
            return True
        
        except:
            return False