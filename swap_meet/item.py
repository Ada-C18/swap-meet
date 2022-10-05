

class Item:
    def __init__(self, category = None, condition = 0):
        self.category = category if category != None else ""
        self.condition = condition

    
    def __str__(self):
        return f"Hello World!"
    
    def condition_description(self) -> str:
        if self.condition == 0:
            return("blegh")
        
        elif self.condition == 1:
            return("meh")
        
        elif self.condition == 2:
            return("eh")
        
        elif self.condition == 3:
            return("ok")
        
        elif self.condition == 4:
            return("not bad")
        
        elif self.condition == 5:
            return("Woah!")


