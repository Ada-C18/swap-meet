import math

class Item:
    def __init__(self, category = "", condition = 0.0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        if math.floor(self.condition) == 0:
            return "damaged"
        elif math.floor(self.condition) == 1:
            return "poor"
        elif math.floor(self.condition) == 2:
            return "average"
        elif math.floor(self.condition) == 3:
            return "good"
        elif math.floor(self.condition) == 4:
            return "mint"
        elif math.floor(self.condition) == 5:
            return "new"