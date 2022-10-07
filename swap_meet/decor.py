from swap_meet.item import Item

class Decor:
    def __init__(self, condition = 0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return f"Something to decorate your space."