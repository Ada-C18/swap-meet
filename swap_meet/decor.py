from swap_meet.item import Item
class Decor:
    def __init__(self, category=None, condition=0.0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."
