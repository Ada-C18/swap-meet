from swap_meet.item import Item

class Clothing:
    def __init__(self, condition = 0):
        self.category = "Clothing"
        self.condition = condition
        self.condition_description = 4

    def __str__(self):
        return f"The finest clothing you could wear."