from unicodedata import category
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition):
        super().__init__("Clothing", condition)


    def __str__(self):
        self.Clothing = "The finest clothing you could wear."
        return self.Clothing


