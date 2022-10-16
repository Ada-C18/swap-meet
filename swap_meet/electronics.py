
from swap_meet.item import Item
class Electronics(Item):
    """Expectation: Has an attribute category that is "Electronics"
    Its stringify method returns "A gadget full of buttons and secrets.
    All three classes and the Item class have an attribute called condition, which can be optionally provided in the initializer. The default value should be 0"""
    
    def __init__(self, condition = 0):
        super().__init__(category = "Electronics", condition = condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
