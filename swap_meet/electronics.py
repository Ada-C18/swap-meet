from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category = "", condition = 0.0):
        self.category = "Electronics"
        self.condition = 0.0
    def __str__(self):
        self.Electronics = "A gadget full of buttons and secrets."
        return self.Electronics
