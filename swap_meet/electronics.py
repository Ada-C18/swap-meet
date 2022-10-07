from swap_meet.item import Item
# creates class/category Electronics using class Item
# stringifies Electronics
class Electronics(Item):
    def __init__(self, category="Electronics", condition=0):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "A gadget full of buttons and secrets."
