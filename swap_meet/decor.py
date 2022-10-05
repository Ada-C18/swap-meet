from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category ="", condition = 0.0):
        self.category = "Decor"

    def __str__(self):
        self.decor = "Something to decorate your space."
        return self.decor