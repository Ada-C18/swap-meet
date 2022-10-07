from .item import Item

class Clothing(Item):
    category = "Clothing"

    def __init__(self, condition = 0):
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."
