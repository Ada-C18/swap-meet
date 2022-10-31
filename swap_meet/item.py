class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        default = "Hello World!"
        return default
    
    def condition_description(self):
        if self.condition == 5:
            return(f"Absolutely Fabulous")
        elif self.condition == 4:
            return(f"Good enough")
        elif self.condition == 3:
            return(f"I'll take it")
        elif self.condition == 2:
            return(f"Decent")
        elif self.condition == 1:
            return(f"Meh")
        elif self.condition == 0:
            return(f"Burn it!")      