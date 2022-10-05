class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 
        

    def __str__(self):
        return "Hello World!" 

    def condition_description(self):
        if self.condition == 0:
            return "mint"
        elif self.condition == 1:
            return "brand new"
        elif self.condition == 2:
            return "almost new"
        elif self.condition == 3:
            return "used"
        elif self.condition == 4:
            return "heavily used"
        elif self.condition == 5:
            return "You probably want a glove for this one..."
            

    
 
            