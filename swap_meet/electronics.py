from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, condition=0.0):
        super().__init__("Electronics", condition)

    def __str__(self):
        super().__str__()
        return "A gadget full of buttons and secrets."
