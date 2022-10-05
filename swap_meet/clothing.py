from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category="Clothing", condition=None):
        self.category = category
        self.condition = condition
        # self.condition = self.condition_description()
        self.condition = condition if condition is not None else 0.0
    def __str__(self):
        return f"The finest clothing you could wear."
    