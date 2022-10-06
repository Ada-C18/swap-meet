import math

class Item:
    def __init__(self, age=None, category="", condition=0):
        self.category = category
        self.condition = condition
        self.age = age


    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        if 0 <= self.condition < 1:
            return "Terrible"
        elif self.condition < 2:
            return "Meh"
        elif self.condition < 3:
            return "Average"
        elif self.condition < 4:
            return "Above Average"
        elif self.condition < 5:
            return "Pretty Good"
        elif self.condition == 5:
            return "Excellent"
