class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Worn down"
        elif self.condition == 1:
            return "Heavily used"
        elif self.condition == 2:
            return "Gently used"
        elif self.condition == 3:
            return "Solid"
        elif self.condition == 4:
            return "Practically perfect"
        elif self.condition == 5:
            return "Never worn before"