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
<<<<<<< HEAD

=======
    
    def get_by_category (self, category):
        matching_items = []
        if category in self.category:
            matching_items.append(category)
        return matching_items
>>>>>>> 48a4704a2810f44d08f76cab97c797bdcdac02c5

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
    # def swap_items(self, vendor, my_item, their_item):
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