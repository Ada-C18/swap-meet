class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        if len(self.inventory) == 0:
            return self.inventory
        else:
            category_items = []
            for item in self.inventory:
                if item.category == category:
                    category_items.append(item)
            return category_items

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in other_vendor.inventory:
            return False
        self.remove(my_item) 
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, another_vendor):
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        my_first_item = self.inventory[0]
        their_first_item = another_vendor.inventory[0]
        result = self.swap_items(another_vendor, my_first_item, their_first_item)
        if result == True:
            return True
