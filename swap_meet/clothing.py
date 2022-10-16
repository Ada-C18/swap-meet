
from swap_meet.item import Item
class Clothing(Item):
    """Expectation: Has an attribute category that is "Clothing"
    Its stringify method returns "The finest clothing you could wear.
    All three classes and the Item class have an attribute called condition, which can be optionally provided in the initializer. The default value should be 0"""
    
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing", condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."
    
