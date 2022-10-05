from swap_meet.item import Item
class Decor:
    def __init__(self, category=None, condition=0):
        self.category = "Decor"
        self.condition = condition
        #super().__init__(category , condition)

    def __str__(self):
        return "Something to decorate your space."
