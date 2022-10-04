from os import remove


class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item

    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False
        else: 
            self.inventory.remove(removed_item)
            return removed_item

    def get_by_category(self,category):
        items_in_category = []
        # item is a object

        for item in self.inventory:
            # item.category  is a string 
            if item.category == category:
                items_in_category.append(item)
            
        return items_in_category

    def swap_items(self, another_vendor_inventory, my_item, their_item):
        if their_item not in another_vendor.inventory or my_item not in self.inventory:
            return False 
        self.inventory.remove(my_item)
        another_vendor_inventory.inventory.remove(their_item)
        another_vendor_inventory.append(my_item)
        self.inventory.append(their_item)
        return True 

"""
removes the my_item from this Vendor's inventory
adds it to the friend's inventory
my_item = representing the item this Vendor instance plans to give
their_item = representing the item the friend Vendor plans to give
"""
    


        



    
