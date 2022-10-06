
class Item:
    def __init__(self, category = "", condition = None):
        self.category = category
        if condition is None: 
            self.condition = 0.0 
        else: 
            self.condition = condition
        
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0: 
            return "Bad condition."
        elif self.condition == 1:
            return "Heavly used."
        elif self.condition == 2:
            return "Been used"
        elif self.condition == 3:
            return "Lightly used."
        elif self.condition == 4: 
            return "Looks new."
        elif self.condition == 5: 
            return "Brand new."
