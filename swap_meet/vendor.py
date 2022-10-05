from operator import attrgetter

#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items
    
        
    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        another_vendor.inventory.append(my_item)
        another_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True

    def swap_first_item(self, another_vendor):
        if not self.inventory or not another_vendor.inventory:
            return False
        self.inventory[0], another_vendor.inventory[0] = another_vendor.inventory[0], self.inventory[0]
        return True

        
    def get_best_by_category(self, category):
        list_items_by_category = self.get_by_category(category)
        best_by_category = max(list_items_by_category, key=attrgetter('condition'))
        return best_by_category
        

        # best_item = max(list_best_category.condition)
        # return best_item
        # get the item with the best condition in a certain category
        # look through the instance's inventory for the item with the highest condition and matching category
        # If there are no items in the inventory that match the category, it returns None
        # It returns a single item even if there are duplicates (two or more of the same item with the same condition)



        

            
        