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
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item):
        """adds given item to the inventory. Returns the item that was added."""

        if isinstance(item, Item):
            self.inventory.append(item)
            return item
        else:
            raise ValueError(f"item argument passed must be of Item type")

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
            if item.category.upper() == category.upper():  #handles edge case of incorrect casing in input
                output_list.append(item)
        return output_list
    
    def swap_items(self, friend, my_item, their_item):
        """swaps one item between the current vendor object and their friends"""
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        """swaps the first item in current vendor object's inventory with
        the first item of friend's inventory list"""
        #edge case: empty inventory list
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False

        temp = self.inventory[0] 
        self.inventory[0] = friend.inventory[0]
        friend.inventory[0]= temp
        return True

    def get_best_by_category(self, category):
        """returns the item with the best condition in a certain category"""
        category = category.upper()
        #edge case: invalid casing of category argument
        if category not in ["CLOTHING", "DECOR", "ELECTRONICS"]:
            return None

        best = 0
        best_item = None
        for item in self.inventory:
            if item.category.upper() == category:
                if item.condition > best:
                    best = item.condition
                    best_item = item
        return best_item  #returns None if no item in the given category is found

    def swap_best_by_category(self, other, my_priority, their_priority):
        """swaps the best item of certain categories with another Vendor"""
        #edge case: if other is not a Vendor instance
        if not isinstance(other, Vendor):
            raise ValueError("other argument passed must be Vendor type object")
        
        #edge case: if one or both vendor's inventory list is empty
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        their_wish = self.get_best_by_category(their_priority)
        my_wish = other.get_best_by_category(my_priority)

        #edge case: if any of the vendor parties have no item of the given category in their inventory
        if not their_wish or not my_wish:
            return False
        
        self.swap_items(other, their_wish, my_wish)
        return True

    def swap_by_newest(self, other):
        """swaps the newest item with another Vendor"""
        #edge case: if any of the vendor parties involved have no inventory 
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        self_newest_item = self.inventory[0]
        self_newest_age = self.inventory[0].age
        
        other_newest_item = other.inventory[0]
        other_newest_age = other.inventory[0].age
        
        # get the newest item for this vendor instance
        for item in self.inventory:
            if item.age < self_newest_age:
                self_newest_age = item.age
                self_newest_item = item

        # get the newest item for the other vendor instance
        for item in other.inventory:
            if item.age < other_newest_age:
                other_newest_age = item.age
                other_newest_item = item
        
        if not other_newest_item or not self_newest_item:
            return False

        #swap the newest item between the 2 vendor instances
        result = self.swap_items(other, self_newest_item, other_newest_item)
        return True


        

        

        

        














    
    







    

    

    


    