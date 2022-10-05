from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    """creates a vendor object with an attribute called "inventory" and 2 methods: 
    "add" that adds items to the inventory, and 
    "remove" that removes item from the inventory."""

    def __init__(self, inventory=None): 
        # Note that inventory is not set to [] as default because 
        # only immutable types should be set as default param.
        #else each instance will share the same value of param.
        """constructor"""
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item):
        """adds given item to the inventory. Returns the item that was added."""
        if isinstance(item, Item) or Item(item):
            self.inventory.append(item)
        elif isinstance(item, list) and len(item) == 1:
            try:
                item = Item(item[0])
                self.inventory.append(item)
                return item
            except ValueError:
                raise ValueError ("invalid type: {item}")
        elif isinstance(item, list) and len(item) > 1:
            for each_item in item:
                try:
                    each_item = Item(each_item)
                    self.inventory.append(each_item)
                except ValueError:
                    raise ValueError("invalid type: {each_item}")  
        else:
            raise ValueError("invalid type: {item}")
        return item

    def remove(self, item):
        """removes given item from the inventory. Returns the item that was removed.
        If the inventory doesn't contain that item, returns False"""
        try: 
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        """returns the item that matches given category."""
        output_list = []
        for item in self.inventory:
            if item.category == category:
                output_list.append(item)
        return output_list
    
    def swap_items(self, friend, my_item, their_item):
        """swaps one item between the current vendor object and their friends"""
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        """swaps the first item in current vendor object's inventory with
        the first item of friend's inventory list"""

        if self.inventory == [] or friend.inventory == []:
            return False
        else:
            temp = self.inventory[0] 
            self.inventory[0] = friend.inventory[0]
            friend.inventory[0]= temp
            return True

    def get_best_by_category(self, category):
        """returns the item with the best condition in a certain category"""
        category = category.upper()
        if category not in ["CLOTHING", "DECOR", "ELECTRONICS"]:
            return None
        else:
            best = 0
            best_item = None
            for item in self.inventory:
                if item.category.upper() == category:
                    if item.condition > best:
                        best = item.condition
                        best_item = item
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """swaps the best item of certain categories with another Vendor"""

        if not isinstance(other, Vendor):
            raise ValueError("{other} is not a vendor object")
        their_wish = self.get_best_by_category(their_priority)
        my_wish = other.get_best_by_category(my_priority)

        if their_wish is None or my_wish is None:
            return False
        else:
            self.swap_items(other, their_wish, my_wish)
            return True












    
    







    

    

    


    