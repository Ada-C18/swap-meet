from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category = None, condition = 0):
        self.category = category
        self.condition = condition
        if self.category is None:
            self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."