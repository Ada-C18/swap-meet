

class Item:
    def __init__(self, category = "", condition = 0):
        self.category= category
        self.condition= condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "It's unusable"
        elif self.condition == 1:
            return "It's still unusable"
        elif self.condition == 2:
            return "Better put it in the trash"
        elif self.condition == 3:
            return "It has some life"
        elif self.condition == 4:
            return "Good condition"
        elif self.condition == 5:
            return "Like new"
        
        






        
