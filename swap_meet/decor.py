from swap_meet.item import Item


class Decor(Item):
    def __init__(self, category = "Decor", condition = None):
        super().__init__(category, condition)

    def __str__(Item):
        return "Something to decorate your space."