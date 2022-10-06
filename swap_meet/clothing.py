from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, age=None, condition=None, category="Clothing"):
        super().__init__(age, condition, category)
    def __str__(self):
        return f"The finest clothing you could wear."