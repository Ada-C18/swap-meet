from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, **kwg):
        super().__init__(**kwg)
        self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."
