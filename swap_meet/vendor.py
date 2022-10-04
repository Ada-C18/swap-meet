from .item import Item



class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item
    
    def get_by_category(self,category = None):
        if category is None:
            category = ""
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)

        return category_items

    

    def swap_items(self, my_item, their_item):
        if 

    
