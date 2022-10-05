class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        """
        Input: item.
        Result: appends item to inventory attribute, a list in class Vendor.
        Also returns item. If item doesn't exist returns False.
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Input: item.
        Result: removes item from inventory attribute, a list in class Vendor.
        Also returns item. If item doesn't exist returns False.
        """
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        
        return item

    def get_by_category(self, a_category):
        """
        Input: category of possible vendor items
        Results/Output: returns list of items with the input category
        """
        items = []
        for item in self.inventory:
            if item.category == a_category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        """
        Input: Second vendor, self's item, second vendors item.

        Results/Output: Return false if either item is not in the
        associated vendors inventory. Returns true and switches items
        if both vendors have the items input.
        """
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:    
            self.remove(my_item)
            friend.add(my_item)
            
            friend.remove(their_item)
            self.add(their_item)
            return True

    def swap_first_item(self, friend):
        """
        Input: Second vendor.
        Results/Output: if both vendors have item(s) in inventory,
        they swap first items in their lists of inventories
        """
        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])
    
    def get_best_by_category(self, category):
        """
        Input: category of item(s).
        Results/Output: returns item with highest condition value within
        a list of items in the same category.
        """
        best_condition = max(self.get_by_category(category), default=None,\
        key=lambda item: item.condition)

        return best_condition

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Input: Second vendor, a category of item self wants, and
        a category of item the second vendor wants.

        Results/Output: swap items of the best condition based on the
        categories each vendor wants.
        """
        they_want = self.get_best_by_category(their_priority)
        i_want = other.get_best_by_category(my_priority)
        
        return self.swap_items(other, they_want, i_want)

    def find_newest_item(self):
        """
        Input: Just call on instance of class Vendor
        Output/Results: Returns newest item in the vendor's inventory
        """
        newest_item = min(self.inventory, default=None,\
        key=lambda item: item.age)

        return newest_item

    def swap_by_newest(self, friend):
        """
        Input: A second vendor.
        Output/Results: Swap newest items between two vendors
        """
        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            return self.swap_items(friend, self.find_newest_item(),\
            friend.find_newest_item())
