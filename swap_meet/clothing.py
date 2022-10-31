from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition) # super to return temp class of clothing
        self.condition = condition

    def __str__(self): # stringify 
        return "The finest clothing you could wear."