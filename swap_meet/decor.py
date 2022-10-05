# - `Decor`
#   - Has an attribute `category` that is `"Decor"`
#   - Its stringify method returns `"Something to decorate your space."`
from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category=None, condition=0):
        super().__init__(category="Decor", condition=condition)
    
    def __str__(self):
        return "Something to decorate your space."