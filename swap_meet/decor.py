from swap_meet.item import Item


class Decor(Item):
    def __init__(self, **kwg):
        super().__init__(**kwg)
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."
