class Item:
    
    def __init__(self, category = None, condition = 0, age = 0):
        self.category = category if category is not None else ""
        self.condition = condition
        self.age = age


    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Heavily Used"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "OK"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Excellent"
        elif self.condition == 5:
            return "Mint"