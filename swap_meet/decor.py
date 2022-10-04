from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category="Decor", condition=None):
        self.category = category
        self.condition = condition if condition is not None else 0.0
    def __str__(self):
        return f"Something to decorate your space."