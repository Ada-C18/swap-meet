class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self, condition):
        if condition == 0:
            return "should be free"
        elif condition == 1:
            return "run over by a car"
        elif condition == 2:
            return "very severly used"
        elif condition == 3:
            return "used"
        elif condition == 4:
            return "gently used, like new"
        elif condition == 5:
            return "mint condition!"