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
        # checks if old_item is in vendor's list
        if old_item in self.inventory:
            # removes old_item from vendor's list and appends it to the provided vendor's list
            self.inventory.remove(old_item)
            vendor.inventory.append(old_item)
            # adds new_item to vendor's list and removes it from the provided vendor's list
            self.inventory.append(new_item)
            vendor.inventory.remove(new_item)
            return True
        else:
            return False