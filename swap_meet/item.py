class Item:
    def __init__(self, category = None, condition = 0):
        if category == None:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return ("Hello World!")

    def condition_description(self):
        if self.condition == 0:
            return "Heavily used"
        elif self.condition == 1:
            return "Pretty used"
        elif self.condition == 2:
            return "Obviously used"
        elif self.condition == 3:
            return "Meh, still has life left"
        elif self.condition == 4:
            return "Light wear"
        elif self.condition == 5:
            return "Minty"