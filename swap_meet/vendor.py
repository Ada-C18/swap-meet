from .item import Item
#Wave1

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        """
        Returns the item added to inventory
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Returns the removed matching item from the inventory 
        or False if no matching item in the inventory.
        """
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    # Wave 2
    
    def get_by_category(self, category = ""):
        """
        Returns a list of Items in the inventory with that category.
        """
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items


    

    