class Item:
    
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        rounded_condition = round(self.condition)

        if self.condition == 0:
            return "You probably want a glove for this one..."
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Excellent"
        elif self.condition == 5:
            return "Mint"