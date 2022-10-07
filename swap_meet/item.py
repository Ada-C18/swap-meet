# from msilib.schema import Condition

class Item:
    def __init__(self,category= "", condition = 0.0):
        self.category = category
        self.condition = condition
        
    def get_category(self):
        return self.category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0.0:
            return "bad"
        elif self.condition <= 1.0:
            return "poor"
        elif self.condition <= 2.0:
            return "acceptable"
        elif self.condition <= 3.0:
            return "fair"
        elif self.condition <= 4.0:
            return "good"
        elif self.condition <= 5.0:
            return "excellent"
    

    