from swap_meet.item import Item

class Decor:
    def __init__(self, condition = None):
        self.category = "Decor"
        if condition == None: 
            self.condition = 0 
        else: 
            self.condition = condition
        
    def __str__(self):
        return "Something to decorate your space."
    
    

