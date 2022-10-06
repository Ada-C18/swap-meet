from .item import Item

class Decor(Item):
    def __init__(self, age=None, condition=0):
        super().__init__(age=age, category="Decor", condition=condition)

    
    def __str__(self):
        return "Something to decorate your space."