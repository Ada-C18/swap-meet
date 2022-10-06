class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "should be free"
        elif self.condition == 1:
            return "run over by a car"
        elif self.condition == 2:
            return "very severly used"
        elif self.condition == 3:
            return "used"
        elif self.condition == 4:
            return "gently used, like new"
        elif self.condition == 5:
            return "mint condition!"