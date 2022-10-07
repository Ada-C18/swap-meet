from swap_meet.item import Item


class Decor(Item):
    def __init__(self, condition = None, age = None):
        super().__init__(category = "Decor", condition = condition, age = age)

    def __str__(Item):
        return "Something to decorate your space."