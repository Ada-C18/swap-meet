'''
WAVE 1

In Wave 1 we will create the `Vendor` class.

- There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`


- Every instance of `Vendor` has an instance method named `add`, which takes in one item
- This method adds the item to the `inventory`
- This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
- This method removes the matching item from the `inventory`
- This method returns the item that was removed
- If there is no matching item in the `inventory`, the method should return `False`
'''
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
# inventory is going to == inventory IF there is a value passed for inventory ELSE it will equal None and return []

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category (self, category):
        if not category:
            return None
        matching_items = []
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            first_own = self.inventory[0]
            first_friend = friend.inventory[0]
            self.swap_items(friend, first_own, first_friend)
            return True
        return False

    def get_best_by_category(self, category):
        inventory = self.get_by_category(category)
        if not inventory:
            return None
        best_item = inventory[0]
        for item in inventory:
            if item.condition > best_item.condition:
                best_item = item.condition
            return best_item
 # for item in inventory:
#     if item.condition == highest:
#         return item
    
    # def test_swap_best_by_category(self, other, my_priority, their_priority):
    #     my_best = self.get_best_by_category(their_priority)
    #     their_best = other.get_best_by_category(my_priority)
    #     if not my_best or not their_best:
    #         return False
    #     return self.swap_items(other, my_best, their_best)


'''
WAVE 3 
Instances of `Vendor` have an instance method named `swap_items`
It takes 3 arguments:
1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
- It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
- It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
- It returns `True`
- If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`
'''
    #     if my_item in own inventory and their_item in friend inventory:
    #       removes my_item from own inventory, adds to friend inventory
    #       removes their_item from friend inventory, adds to own
    #       return True
    #     else: (if I or they don't have an item)
    #       return False

'''
WAVE 4

- Instances of `Vendor` have an instance method named `swap_first_item`
- It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
- This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
- It removes the first item from its `inventory`, and adds the friend's first item
- It removes the first item from the friend's `inventory`, and adds the instances first item
- It returns `True`
- If either itself or the friend have an empty `inventory`, the method returns `False`
'''
    # def swap_first_item(self, vendor):
    #   If own inventory or friends inventory is not empty:
    #       removes first item from own inventory + adds friends first item
    #       removes first item from friends inventory + adds own first item
    #       return True
    #   else:
    #       return False
'''
WAVE 6

Vendors have a method named get_best_by_category, which will get the item with the best condition in a certain category
It takes one argument: a string that represents a category
This method looks through the instance's inventory for the item with the highest condition and matching category
It returns this item
If there are no items in the inventory that match the category, it returns None
It returns a single item even if there are duplicates (two or more of the same item with the same condition)
'''

    # def get_best_by_category(self, category):
    #     inventory = self.get_by_category(category)
    #     if inventory is None:
    #         return None
    #     highest = 0
    #     for item in inventory: 
    #         if item.condition > highest:
    #             highest = item.condition
    #         return item
            
        # self.get_by_category(category) | if category = "Clothing", return list of items that match
        # if item rating = highest rating | for 
        # if item listed > item given, 

'''
WAVE 6
Vendors have a method named swap_best_by_category, which will swap the best item of certain categories with another Vendor
It takes in three arguments
other, which represents another Vendor instance to trade with
my_priority, which represents a category that the Vendor wants to receive
their_priority, which represents a category that other wants to receive
The best item in my inventory that matches their_priority category is swapped with the best item in other's inventory that matches my_priority
It returns True
If the Vendor has no item that matches their_priority category, swapping does not happen, and it returns False
If other has no item that matches my_priority category, swapping does not happen, and it returns False
'''
