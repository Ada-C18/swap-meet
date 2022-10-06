# from swap_meet.item import Item

class Electronics:
    def __init__(self, condition = None):
        self.category = "Electronics"
        if condition == None: 
            self.condition = 0 
        else: 
            self.condition = condition
        
    def __str__(self):
        return "A gadget full of buttons and secrets."

    
    
