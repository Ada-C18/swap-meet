from swap_meet.item import Item

class Decor:
    def __init__(self, category = "Clothing", condition = '0'):
        super().__init__(condition="0")
        self.category = category

    def __str__(self):
        return "Something to decorate your space."