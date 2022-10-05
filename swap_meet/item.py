class Item:
    def __init__(self, category=""):
        self.category = category
    def __str__(self):
        return ("Hello World!")

# In Wave 2 we will create the `Item` class and the `get_by_category` method.

# - There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

# - Inside this module, there is a class named `Item`
# - Each `Item` will have an attribute named `category`, which is an empty string by default
# - When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`



# In Wave 3 we will write a method to stringify an Item using str() and write the method swap_items.

# When we stringify (convert to a string) an instance of Item using str(), it returns "Hello World!"
# This implies Item overrides its stringify method. We may need to research the __str__ method for more details!
# The remaining tests in wave 3 imply:

# Instances of Vendor have an instance method named swap_items
# It takes 3 arguments:
# an instance of another Vendor, representing the friend that the vendor is swapping with
# an instance of an Item (my_item), representing the item this Vendor instance plans to give
# an instance of an Item (their_item), representing the item the friend Vendor plans to give
# It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
# It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
# It returns True
# If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False