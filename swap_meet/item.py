class Item:
    def __init__(self,category = "", condition = 0.0):
        self.category = category
        self.condition = condition
    
        

    def __str__(self):
        return "Hello World!"

    

    def condition_description(self):

        if self.condition >= 5:
            return "mint"
        elif self.condition >= 4:
            return "Not Happy about it"
        elif self.condition >= 3:
            return "The Brand is new"
        elif self.condition >= 2:
            return "heavily used"
        elif self.condition >= 1:
            return "You probably want a glove for this one."
        elif self.condition >= 0:
            return "Check your list of items"
        
