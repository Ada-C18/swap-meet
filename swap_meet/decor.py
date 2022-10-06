from swap_meet.item import Item


class Decor(Item):
    def __init__(self, condition=0.0):
        super().__init__("Decor", condition)

    def __str__(self):
        super().__str__()
        return "Something to decorate your space."
