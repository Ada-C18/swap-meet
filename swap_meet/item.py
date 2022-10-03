from unicodedata import category


class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition = self.condition
        if condition < 1:
            return "This item is heavily used."
        elif condition < 2:
            return "This item is in fair condition."
        elif condition < 3:
            return "This item is in good condition with normal use signs."
        elif condition < 4:
            return "This item is in great condition with limited faint signs of wear."
        elif condition < 5:
            return "This item is in like new condition."
        else:
            return "This is a brand new item."