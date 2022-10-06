from .item import Item


class Electronics(Item):
    # grab initial conditions from Item class,
    # change default category to "Electronics"
    def __init__(self, category="Electronics", condition=0):
        super().__init__(category, condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
