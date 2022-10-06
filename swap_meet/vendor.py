from .item import Item

class Vendor(Item):
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


# ******** Wave 2 ********
    def get_by_category(self,category = None):
        if category is None:
            category = ""
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)

        return category_items


# ******** Wave 3 ********
    def swap_items(self, vendor, my_item, their_item):
        if self.inventory == [] or vendor.inventory == []:
            return False
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.inventory.remove(my_item)
        vendor.inventory.remove(their_item)

        self.inventory.append(their_item)
        vendor.inventory.append(my_item)
        
        return True 

# ******** Wave 4 ********
# option1 : with helper functions - swap_items()
    def swap_first_item(self, vendor):
        if self.inventory == [] or vendor.inventory == []:
            return False
        my_item = self.inventory[0]
        their_item = vendor.inventory[0]
        self.swap_items(vendor, my_item, their_item)
        return True

# option2 : without helper functions
    # def swap_first_item(self, vendor):
    #    if self.inventory == [] or vendor.inventory == []:
    #         return False
        # temp1 = self.inventory.pop(0)
        # temp2 = vendor.inventory.pop(0)

        # vendor.inventory.append(temp1)
        # self.inventory.append(temp2)
        # return True 

# ******** Wave 6 ********
    def get_best_by_category(self, category):
        best_condition = 0
        category_items = self.get_by_category(category)

        for item in category_items:
            if item.condition > best_condition:
                best_condition = item.condition
          
        for item in category_items:
            if item.condition == best_condition:
                return item
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        their_category_items = other.get_by_category(my_priority)  
        if their_category_items ==[]:
            return False
        my_category_items = self.get_by_category(their_priority)  
        if my_category_items ==[]:
            return False
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category( my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        
        
