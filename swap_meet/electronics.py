from .item import Item

class Electronics(Item):
    def __init__(self, age=None, condition=0):
        super().__init__(age=age, category="Electronics", condition=condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
