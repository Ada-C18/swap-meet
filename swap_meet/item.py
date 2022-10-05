# ******** Wave 3 ********
class Item:
    def __init__(self, category=None, condition = 0):
        if category is None:
            category = ""
        self.category = category
        self.condition = 0
 
        
    def __str__(self):
        return "Hello World!"


# ******** Wave 4 ********
    def condition_description(self):
        if self.condition > 5 or self.condtion < 0:
            return "please enter condition:  0~5"
        elif self.condition >= 4:
            return "Excellent"
        elif self.condition >= 3:
            return "Good"
        elif self.condition >= 2:
            return "Well used"
        else:
            return "heavily used"
        