import pytest


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

    #return a list of items that the vendor has in a given category  
    def get_by_category(self, category):
        # category_list = filter(lambda item: item.category == category, self.inventory)
      
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)

        return category_list

    """
    Swap_items vendor method checks if the items are in each vendor's inventory,
    then removes and adds items from both vendor's inventories.
    """
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item) and other_vendor.remove(their_item)
            self.add(their_item) and other_vendor.add(my_item)
            return True

    """
    swap_first_item function using swap_item method with inventory index position 
    """

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) ==0:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    """
    get_best_by_category class method returns the item with the best condiiton filtered by the category argument
    """
    
    def get_best_by_category(self, category):
        items_by_category_list = self.get_by_category(category)
        if len(items_by_category_list) > 0:
            best_in_category = max(items_by_category_list, key=lambda item: item.condition)
            return best_in_category


    """
    swap_best_by_category method
    """
    def swap_best_by_category(self, other, my_priority, their_priority):
        #use len of get_by_category to return false if either vendor does not have the other's preference
        if len(self.get_by_category(their_priority)) == 0 or len(other.get_by_category(my_priority)) == 0:
            return False
        
        #use get_best_by_category to assign variables to each item to swap
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        #use swap_items to move the items between the vendors
        self.swap_items(other, my_item, their_item)
        return True

    """
    use find_newest method to identify the item with the smallest age in each vendor's inventory
    creat swap by newest method that will pass each newest item into the swap method
    """
    
    def find_newest(self):
        newest_item = min(self.inventory, key = lambda item: item.age)
        return newest_item

    
    def swap_by_newest(self, other_vendor):
        if len(other_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
        
        my_newest_item = self.find_newest()
        their_newest_item = other_vendor.find_newest()

        return self.swap_items(other_vendor, my_newest_item, their_newest_item)
