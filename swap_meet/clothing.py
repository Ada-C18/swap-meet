# ******** Wave 5 ********
from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        
        self.category = "Clothing"
        self.condition = condition
        

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        super().condition_description(self)
