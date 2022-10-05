from swap_meet.item import Item
class Electronics:
    def __init__(self,category, condition = '0'):
        self.category = "Electronics"

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."