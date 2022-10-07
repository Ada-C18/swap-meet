from swap_meet.item import Item

class Electronics:
    def __init__(self, condition = 0):
        self.category = "Electronics"
        self.condition = condition

    def __str__(self):
        return f"A gadget full of buttons and secrets."
