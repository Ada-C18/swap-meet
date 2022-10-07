
# from attr import NOTHING

class Item:
    def __init__(self, category = "", condition=None, age = None):
        if not condition:
            condition = 0.0
        self.condition = condition
        self.category = category
        if not age:
            age = 0
        self.age = age
        
        
    def __str__ (self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition >= 0 and self.condition <=2:
            return "Condition: imperfect"
        elif self.condition >=3 and self.condition <=4:
            return "Condition: gently used"
        else:
            return "Condition: like new"
        