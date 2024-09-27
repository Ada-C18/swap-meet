# - `Clothing`
#   - Has an attribute `category` that is `"Clothing"`
#   - Its stringify method returns `"The finest clothing you could wear."`
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__(category ="Clothing", condition=condition)
    
    def __str__(self):
        return "The finest clothing you could wear."