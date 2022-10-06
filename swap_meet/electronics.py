from .item import Item

class Electronics(Item):
    def __init__(self, category="Electronics", condition=0):

        # pass variables to the super().__init__ function
        # including the default category. 
        super().__init__(category=category, condition=condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
