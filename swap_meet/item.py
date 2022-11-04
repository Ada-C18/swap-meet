# from attr import validate

class Item:
    def __init__(self, category = None, condition = 0):
        #  category is an empty string
        if category is None:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 0 and self.condition < 2:
            return "1 star"
        elif self.condition > 1 and self.condition < 3:
            return "2 stars"
        elif self.condition > 2 and self.condition < 3:
            return "3 stars"
        elif self.condition > 4 and self.condition < 5:
            return "4 stars"
        elif self.condition == 5:
            return "5 stars"
        else:
            return "Invalid number"

        
        

    
    
    
        
        