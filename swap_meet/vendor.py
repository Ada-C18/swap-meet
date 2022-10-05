
class Vendor:
    def __init__(self, inventory=None):
        '''
        takes in an inventory list of items and will create an instance of Vendor
        '''
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        '''
        Input: item
        Returns item

        Will take in an item to add to vendor's inventory
        '''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''
        Input: item
        Returns item or False

        Will take in an item to remove from vendor's inventory
        If item is not in vendor's inventory, will return False
        '''
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category): 
        '''
        Input: category
        Return list of items in that category

        Will take in a category and will return a list of items within that category
        If no items in the category, will return False
        '''
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        '''
        Input: other_vendor, my_item, their_item
        Return True if able to swap, False if not able to swap 

        Will swap my_item from vendor instance calling the function with their_item from vendor inputted.
        '''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            # self.add(their_item)
            # vendor.add(my_item)
            # vendor.remove(their_item)
            # self.remove(my_item)
            self.add(vendor.remove(their_item))
            vendor.add(self.remove(my_item))
            return True

    def swap_first_item(self, vendor):
        '''
        Input: other_vendor, my_item, their_item
        Return True if able to swap, False if not able to swap 

        Will swap first item from inventory of vendor instance calling the function,
        with the first item from inventory of vendor inputted.
        '''
        if self.inventory and vendor.inventory:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            # self.add(vendor.remove(vendor.inventory[0]))
            # vendor.add(self.remove(self.inventory[0]))
            return True
        return False
        
    def get_best_by_category(self, category):
        '''
        Input: Category 
        Return: best condition item 
        will take in a category and return the item with the best condition
        '''
        best_condition = -1
        best_item = None
        
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: other vendor, my priority category, their priority category
        Return: True if successfully swapped, False if unsuccessful 
        will swap best condition item in respective parties desired category
        '''
        if not self.get_by_category(their_priority) or not other.get_by_category(my_priority):
            return False
        else:
            self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))
            return True    
    
    def get_newest(self):
        '''
        Return newest item or False if inventory is empty 
        will find the newest item in the inventory
        '''
        if len(self.inventory) > 0:
            newest = self.inventory[0]
            youngest_age = self.inventory[0].age
            for item in self.inventory:
                if item.age < youngest_age:
                    youngest_age = item.age
                    newest = item
            return newest
        return False

    def swap_by_newest(self, other):
        '''
        Return newest item or False if inventory is empty 
        will swap the newest items in each vendor's inventory
        '''
        if self.inventory and other.inventory:
            # self_newest = self.get_newest()
            # other_newest = other.get_newest()
            return self.swap_items(other, self.get_newest(), other.get_newest())
        return False
        


