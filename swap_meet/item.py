'''
In Wave 2 we will create the `Item` class and the `get_by_category` method.

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

- Inside this module, there is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default
- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`

- Instances of `Vendor` have an instance method named `get_by_category`
- It takes one argument: a string, representing a category
- This method returns a list of `Item`s in the inventory with that category
'''

class Item:
    def __init__(self, category=None, condition=0):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition


    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Horrible Condition"
        elif self.condition == 1:
            return "Heavily Used"
        elif self.condition == 2:
            return "So-So condition"
        elif self.condition == 3:
            return "Decent"
        elif self.condition == 4:
            return "Gently Used"
        elif self.condition == 5:
            return "Like New!"
        
# book = Item("book", "literature", 5)

'''
In Wave 3 we will write a method to stringify an `Item` using `str()` and write the method `swap_items`.

- When we stringify (convert to a string) an instance of `Item` using `str()`, it returns `"Hello World!"`
- This implies `Item` overrides its stringify method. We may need to research the `__str__` method for more details!
'''

