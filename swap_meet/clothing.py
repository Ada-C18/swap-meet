
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, Clothing, condition = 0):

        super().__init__(condition)
        self.category = Clothing 



    def __str__(self):
        return "The finest clothing you could wear."
