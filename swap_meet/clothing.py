from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(self, condition)
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return f"The finest clothing you could wear."