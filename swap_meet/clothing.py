from unicodedata import category
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(self, condition, category= "Clothing")
        self.condition = condition
    def __str__(self) -> str:
        return "The finest clothing you could wear."
    