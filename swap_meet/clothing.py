from .item import Item
class Clothing(Item):
    def __init__(self, condition):
        super().__init__(condition, condition)
        self.category = "Clothing"
        
    def __str__(self):
        return "The finest clothing you could wear."