from unicodedata import name


class Item:
    # each item will have attribute- empty list by default
    def __init__(self, category= None):
        self.category = category if category is not None else ""
    
    # make a string method that always return Hello World!
    def __str__(self):
        return "Hello World!"
