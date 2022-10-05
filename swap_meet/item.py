class Item:
    def __init__ (self, category="", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "extremly used"
        if self.condition >= 1 and self.condition < 2:
            return "used"
        if self.condition >= 2 and self.condition < 3:
            return "ok condition"
        if self.condition >= 3 and self.condition < 4:
            return "almost new"
        if self.condition >=4:
            return "good as new"
        
# In Wave 2 we will create the `Item` class and the `get_by_category` method.

# - There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

# - Inside this module, there is a class named `Item`
# - Each `Item` will have an attribute named `category`, which is an empty string by default
# - When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
