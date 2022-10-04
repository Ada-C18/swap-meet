# Wave 2, 5
#=========================================
class Item:
    def __init__(self, category = "", condition = 0):
        if condition:
            self.condition = condition
        else:
            self.condition = 0
        if category:
            self.category = category
        else:
            self.category = ""

# Wave 3
#=========================================   
    # write stringify method that returns "Hello World!"
    def __str__(self):
        return "Hello World!"

# Wave 5
#=========================================  
    def condition_description(self):
        if self.condition == 0:
            return "Wouldn't wear this if offered money"
        elif self.condition == 1:
            return "Heavily used"
        elif self.condition == 2:
            return "Moderately used"
        elif self.condition == 3:
            return "Lightly used"
        elif self.condition == 4: 
            return "Like new"
        elif self.condition == 5:
            return "New"