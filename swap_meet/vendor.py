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
        # item_category = Item(category=self.category)
        for item in self.inventory:
            # item_category = Item(category=self.category)
            # if item.category == item_category.category:
            if item.category  == category:
                items_in_category.append(item)
        return items_in_category
    
    def swap_items(self, vendor, my_item, their_item):
        self.vendor = vendor
        self.my_item = my_item
        self.their_item = their_item
        my_items = Vendor(self.inventory)
        if my_item not in my_items.inventory or their_item not in vendor.inventory:
            return False
        my_items.remove(my_item)
        my_items.add(their_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True
    
    def swap_first_item(self, vendor):
        self.vendor = vendor
        if not self.inventory or not vendor.inventory:
            return False
        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])



    #     items_in_category = []
    #     for i in self.inventory:
    #         if i == Item(category=category):
    #             items_in_category.append(i)
        
    #     return items_in_category

        
        # Item.category



