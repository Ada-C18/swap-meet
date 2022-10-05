from .item import Item

class Decor(Item):
    def __init__(self, category="Decor", condition=0):

        # pass variables to the super().__init__ function
        # including the default category. 
        super().__init__(category=category, condition=condition)

    def __str__(self):
        return "Something to decorate your space."