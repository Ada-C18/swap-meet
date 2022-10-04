from .item import Item
# from swap_meet.item import Item


# class Clothing:
class Clothing(Item):
    def __init__(self, category="", condition=0):
        super().__init__(category, condition)
        self.category = "Clothing"

    def __str__(self):
        super().__str__()
        return "The finest clothing you could wear."
