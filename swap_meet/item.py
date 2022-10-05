
class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):   #when you see a print statement that is on an object of class item, call this method!
        return f"Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Re-consider"
        elif self.condition == 1:
            return "its super old"
        elif self.condition == 2:
            return "its old"
        elif self.condition == 3:
            return "its ok"
        elif self.condition == 4:
            return "get it!" 
        elif self.condition == 5:
            return "like new"
        #----do this in a for loop---
        # for the_condition in self.condition in range(0,6):
        #     if self.conditon == 0:
        #         return "re-consider getting this!"
        #     elif self.condition > 0 and self.condition < 3:
        #         return "its okay"
        #     elif self.condition > 3 and self.condition < 5:
        #         return "its wonderfult"
