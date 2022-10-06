from .item import Item

class Clothing(Item):
    def __init__(self, age=None, condition=0):
        super().__init__(age=age, category="Clothing", condition=condition)

    def __str__(self):
        return "The finest clothing you could wear."