from swap_meet.item import Item
class Decor(Item):
    def __init__(self, age, condition=None, category="Decor"):
        super().__init__(age, condition, category)
    def __str__(self):
        return f"Something to decorate your space."