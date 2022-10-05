from pickle import FALSE
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
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

    def get_by_category(self, item_category):
        self.category =  item_category 
        items_in_category = []
        if item.category == self.category:
            items_in_category.append(item.category)

    def get_by_category(self, category=""):
        items = []
        for Item in self.inventory:
            if category == Item.category:
                items.append(Item)

        return items
    
    def swap_items(self, Vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in Vendor.inventory:
            return False
        else:
            self.remove(my_item)
            Vendor.add(my_item)
            Vendor.remove(their_item)
            self.add(their_item)
            return True
