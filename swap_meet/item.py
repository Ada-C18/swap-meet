class Item:
    def __init__(self, condition = 0.0, category = ""):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1.0:
            return "This should be trash"
        elif self.condition < 2.0:
            return "Needs a lot of love and repairs"
        elif self.condition < 3.0:
            return "Acceptable with low standards"
        elif self.condition < 4.0:
            return "Fair condition"
        elif self.condition < 5.0:
            return "Gently used"
        elif self.condition == 5.0:
            return "Mint condition!"