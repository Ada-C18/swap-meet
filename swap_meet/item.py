class Item:
    """creates an Item object with an attribute called 'category'."""
    def __init__(self, age = 1, category = "", condition = 0):
        self.age = age
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 5:
            return "Mint"
        elif self.condition == 4:
            return "like new"
        elif self.condition == 3:
            return "good/gently used"
        elif self.condition == 2:
            return "used/some wear and tear"
        elif self.condition == 1:
            return "used/as is"
        elif self.condition == 0:
            return "heavily used/might have broken or missing parts"
        else:
            raise ValueError("condition must be between 0 to 5.")
        





