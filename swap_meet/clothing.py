#~~~~~~~~~~~~~~~~~~~~~~~ WAVE 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Clothing:
    def __init__(self):
        self.category = "Clothing"
        self.condition = 0

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        if self.condition == 0:
            return "Heavily used; almost vintage."
        elif self.condition == 1:
            return "Has some life left to live."
        elif self.condition == 2:
            return "It could be worse.."
        elif self.condition == 3:
            return "You could do better."
        elif self.condition == 4:
            return "In great shape!"
        elif self.condition == 5:
            return "Brand new."