# In Wave 2 we will create the `Item` class and the `get_by_category` method.


# - Each `Item` will have an attribute named `category`, which is an empty string by default
# - When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`


class Item:
    def __init__(self, category=None):
        self.category = category if category is not None else ""
    
    
        