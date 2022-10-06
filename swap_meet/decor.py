from .item import Item


class Decor(Item):
    # grab initial conditions from Item class,
    # change default category to "Decor"
    def __init__(self, category="Decor", condition=0):
        super().__init__(category, condition)

    def __str__(self):
        return "Something to decorate your space."
