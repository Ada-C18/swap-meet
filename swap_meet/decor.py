from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category = None, condition = 0):
        self.category = category
        self.condition = condition
        if self.category is None:
            self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."
    
    