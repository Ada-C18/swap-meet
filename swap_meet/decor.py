from .item import Item

class Decor(Item):
    category = "Decor"

    def __init__(self, condition = 0):
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."