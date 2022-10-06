# from swap_meet.item import Item
# an instance of Item tells you the class 

class Item:
    def __init__(self, category = "", condition = None):
        self.category = category
        if condition is None: 
            self.condition = 0.0 
        else: 
            self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
