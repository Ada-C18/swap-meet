#import swap_meet

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        #Adds item to the vendor's inventory
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        #Removes item from the vendor's inventory if it is in the inventory list
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        #Returns a list of the vendor's items that have the same category as the argument
        items = [item for item in self.inventory if category == item.category]
        return items

    def swap_items(self, other_vendor, self_item, other_vendor_item):
        #Returns false if vendor's swap item is not in vendor's inventory 
        #or if vendor2's swap item is not in vendor2's inventory
        if self_item not in self.inventory or other_vendor_item not in other_vendor.inventory:
            return False
        #Adds vendor2's swap item and removes vendor's swap item from vendor's inventory
        self.inventory.append(other_vendor_item)
        self.inventory.remove(self_item)
        #Adds vendor's swap item and removes vendor2's swap item from vendor2's inventory
        other_vendor.inventory.append(self_item)
        other_vendor.inventory.remove(other_vendor_item)
        return True

    def swap_first_item(self, other_vendor):
        #do I need a clause for if self.inventory or other_vendor_inventory not empty
        self_first_item=self.inventory[0]
        other_vendor_first_item=other_vendor.inventory[0]
        result=self.swap_items(other_vendor, self_first_item, other_vendor_first_item)
        return result
        
        
        #re-use code o
        
        

