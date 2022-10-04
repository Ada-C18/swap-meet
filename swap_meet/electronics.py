from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category="Electronics", condition=None):
        self.category = category
        self.condition = condition if condition is not None else 0.0
    def __str__(self):
        return f"A gadget full of buttons and secrets."
