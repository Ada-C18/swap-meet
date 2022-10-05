from swap_meet.item import Item
class Decor(Item):
    def __init__(self, condition=None, category="Decor"):
        super().__init__(condition, category)
    def __str__(self):
        return f"Something to decorate your space."