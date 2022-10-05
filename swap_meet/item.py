CONDITION_DESCRIPTION = {
    0:"heavily used",
    1:"well loved",
    2:"almost new",
    3:"medium used",
    4:"open box",
    5:"mint"
    }

class Item:
    def __init__(self,category="",condition =0,age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!" 

    def condition_description(self):
        for key, value in CONDITION_DESCRIPTION.items():
            if self.condition is key:
                return value  
        
        
                             
