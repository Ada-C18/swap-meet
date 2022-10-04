from swap_meet.item import Item

class Clothing(Item):

# Wave 5 
    def __init__(self, condition = 0.0):
        self.category = "Clothing"

    def __str__ (self):
        return "The finest clothing you could wear."
