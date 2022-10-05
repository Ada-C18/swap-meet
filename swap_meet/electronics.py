from .item import Item
class Electronics(Item):
    def __init__(self, condition):
        super().__init__(condition, condition)
        self.category = "Electronics"
        
        
    def __str__(self):
        return "A gadget full of buttons and secrets."
