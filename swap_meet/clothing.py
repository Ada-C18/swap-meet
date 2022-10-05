from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0, age = 0):
        super().__init__(category, condition, age)
    def __str__(self):
        self.str = "The finest clothing you could wear."
        return self.str