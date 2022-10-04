class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "This should be trash"
        if self.condition == 1:
            return "Needs a lot of love and repairs"
        if self.condition == 2:
            return "Acceptable with low standards"
        if self.condition == 3:
            return "Fair condition"
        if self.condition == 4:
            return "Gently used"
        if self.condition == 5:
            return "Mint condition!"