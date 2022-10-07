from swap_meet.item import Item

class Decor(Item):

# Wave 5    
    def __init__(self, condition = 0.0):
        self.category = "Decor"
        self.condition = condition
        
        #super().__init__("Decor", condition, age)
   
    def __str__(self):
        return "Something to decorate your space."