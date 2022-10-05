from swap_meet.item import Item

class Decor(Item):
    super().__init__(category = "Decor")
    def __str__(self):
        return "Something to decorate your space."
    