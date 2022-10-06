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

    def swap_first_item(self, Vendor):
        if len(self.inventory) < 1 or len(Vendor.inventory) < 1: 
            return False 
        else:
            item_1 = self.inventory[0]
            item_2 = Vendor.inventory[0]
            self.inventory[0] = item_2
            Vendor.inventory[0] = item_1
            return True

### Wave 6

# In Wave 6 we will write two methods, `get_best_by_category` and `swap_best_by_category`.

# - `Vendor`s have a method named `get_best_by_category`, which will get the item with the 
# best condition in a certain category
#   - It takes one argument: a string that represents a category
#   - This method looks through the instance's `inventory` for the item with the highest 
# `condition` and matching `category`
#     - It returns this item
#     - If there are no items in the `inventory` that match the category, it returns `None`
#     - It returns a single item even if there are duplicates (two or more of the same item
#  with the same condition)
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best_item = ''
        best_condition = 0
        for item in items:
            if item.condition > best_condition:
                best_item = item 
                best_condition = item.condition 
        return best_item
            

