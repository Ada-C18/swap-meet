from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category=None, condition=0):
        self.category = "Electronics"
        self.condition = float(condition)

        # how to use super() to reuse condition from Item?

    def __str__(self):
        return "A gadget full of buttons and secrets."
