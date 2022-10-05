from .item import Item
class Decor(Item):
    def __init__(self, condition):
        super().__init__(condition, condition)
        self.category = "Decor"
        
    def __str__(self):
        return "Something to decorate your space."