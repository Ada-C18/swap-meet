from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        '''A blueprint for different store inventories.'''
        if inventory is None:
            inventory = [] 
        self.inventory = inventory
    
    def add(self, item):
        '''Add an item to the inventory list.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Remove an item from inventory list.'''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        category_list = []
        for i in self.inventory:
            if i.category == category:
                category_list.append(i)
        return category_list
            
    def swap_items(self, other_vendor, my_item, their_item):
        '''Remove an item from this Vendor's inventory and swaps
        with other vendor.'''
        # remove and append
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            return True
        else:
            return False 

    def swap_first_item(self, other_vendor):
        '''Swap the first item in this vendor's inventory with
        first item of other vendor.'''
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        '''Returns item with the best condition in a certain category.'''
        list_of_items_of_category = self.get_by_category(category)
        if not list_of_items_of_category:
            return None

        condition_max = 0
        best_item = ""
        for item in list_of_items_of_category:
            if item.condition > condition_max:
                condition_max = item.condition
                best_item = item
        
        return best_item
        

        # condition_max = 0
        # best_item = ""
        # for item in self.inventory:
        #     category_counter = 0
        #     if item.category == category:
        #         category_counter += 1
        #         if item.condition > condition_max:
        #             condition_max = item.condition
        #             best_item = item
    
        # if category_counter == 0:
        #     return None
        # else:
        #     return best_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Swap best item of certain categories with another vendor.'''
        # use swap_items function
        # swap best item in my inventory that matches their_priority
        # swap best item in other inventory that matches my_priority
        # return true
        # if have no matching category for either person, return false
        
        # if not self.inventory or not other.inventory:
        #     return False

        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        
        if my_item is None or their_item is None:
            return False

        self.swap_items(other, my_item, their_item)
        return True
