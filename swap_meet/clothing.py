
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, category = 0, condition = 0):

        super().__init__(condition = 0)
        self.category = "Clothing" 



    def __str__(self):
        return "The finest clothing you could wear."
