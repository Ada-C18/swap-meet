from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__(self, condition)
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return f"Something to decorate your space."