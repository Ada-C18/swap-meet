from .item import Item

class Decor(Item):
    
    def __init__(self, category = "", condition=0):
        self.category = "Decor"
    
    def __str__(self):
        return "Something to decorate your space."