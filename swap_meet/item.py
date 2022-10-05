

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "The best you can get."
        if self.condition == 4:
            return "It's quality."
        if self.condition == 3:
            return "It's good enough."
        if self.condition == 2:
            return "Not sure on this one."
        if self.condition == 1:
            return "Another person's trash might be someone's treasure?"
        if self.condition == 0:
            return "I would just throw this out."



