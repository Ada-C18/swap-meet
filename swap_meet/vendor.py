from swap_meet.item import Item
class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item
    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    # create get_by_cateogry instance method that takes in category argument

    def get_by_category(self, category):
    #     # reutrn list of items by category
        self.category = category
        items_in_category = []
        # instance from item class
        item_category = Item(category=self.category)
        for item in self.inventory:
            # item_category = Item(category=self.category)
            if item.category == item_category.category:
                items_in_category.append(item)
        return items_in_category


    #     items_in_category = []
    #     for i in self.inventory:
    #         if i == Item(category=category):
    #             items_in_category.append(i)
        
    #     return items_in_category

        
        # Item.category



