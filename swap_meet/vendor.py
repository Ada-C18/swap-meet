from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        # adds provided item to the vendor's inventory
        self.inventory.append(item)
        # provides the index position of the new item
        index = len(self.inventory) - 1
        # returns the item from the inventory list
        return self.inventory[index]

    def remove(self, item):
        # checks if item is in vendor's inventory list
        if item in self.inventory:
            # removes item if in list
            self.inventory.remove(item)
            return item
        # returns False if item not in list
        else:
            return False

    def get_by_category(self, category):
        # creates blank list for the specific category of items
        category_items = []
        # looks at each item in inventory and if the category matches, appends it to category_items
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        # returns the list of items from requested category
        return category_items

    def swap_items(self, vendor, old_item, new_item):
        # checks if old_item is in inventory list and if new_item is in vendor's inventory list
        if old_item in self.inventory and new_item in vendor.inventory:
            # removes old_item from inventory list and appends it to the vendor's inventory list
            self.inventory.remove(old_item)
            vendor.inventory.append(old_item)
            # adds new_item to inventory list and removes it from the vendor's inventory list
            self.inventory.append(new_item)
            vendor.inventory.remove(new_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        # checks if either inventories are empty and returns False if true
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        # removes index 0 from both lists and adds to opposite list
        else:
            vendor.inventory.append(self.inventory.pop(0))
            self.inventory.append(vendor.inventory.pop(0))
            return True

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        best_item = Item()
        for item in category_items:
            if item.condition >= best_item.condition:
                best_item = item
        return best_item