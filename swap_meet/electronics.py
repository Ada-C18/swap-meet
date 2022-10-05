from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, condition=None, category="Electronics"):
        super().__init__(condition, category)
    def __str__(self):
        return f"A gadget full of buttons and secrets."