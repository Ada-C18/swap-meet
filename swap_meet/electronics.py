# - `Electronics`

#   - Has an attribute `category` that is `"Electronics"`
#   - Its stringify method returns `"A gadget full of buttons and secrets."`
from unicodedata import category
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0.0):
        super().__init__(category="Electronics", condition=condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
