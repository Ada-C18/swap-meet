from swap_meet.item import Item

class Electronics:
    def __init__(self, category="Electronics", condition=0):
        self.category = category
        self.condition= condition

    def __str__ (self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        if self.condition == 0:
            return "poor"
        elif self.condition == 1:
            return "fair"
        elif self.condition == 2:
            return "good"
        elif self.condition == 3:
            return "excellent"
        elif self.condition == 4:
            return "perfect"
        elif self.condition == 5:
            return "new"
