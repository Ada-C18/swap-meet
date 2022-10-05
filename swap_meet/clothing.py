from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = None):
        super().__init__(condition, category = "Clothing")
#       super().__init__(condition, category = "Clothing") # default arg has to be at the end
        
    
    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        