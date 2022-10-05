from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category=None, condition=0):
        self.category = "Clothing"
        self.condition = float(condition)

    def __str__(self):
        return "The finest clothing you could wear."