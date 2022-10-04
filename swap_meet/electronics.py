<<<<<<< HEAD
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category ="Electronics", condition = 0):
=======
class Electronics:
    def __init__(self, category ="Electronics", condition = 0.0):
>>>>>>> 30ebb9904bf0ed23215518c8d1ec803c7f46d6f0
        self.category = category

    def __str__(self):
        return f"A gadget full of buttons and secrets."

    def condition_description(self):
        return f"{self.condition}"
