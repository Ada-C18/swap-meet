from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0.0, age = 0, size = "n/a"):
        super().__init__("Clothing", condition, age)
        self.size = size 

    def __str__(self): 
        return "The finest clothing you could wear."