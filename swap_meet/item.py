class Item:
    def __init__(self, category = "", condition=0):
        self.category = category 
        self.condition = condition 
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        rating = self.condition 
        if rating == 0:
            return "very gross"
        elif rating == 1: 
            return "Not that great"
        elif rating == 2:
            return "It's okay..."
        elif rating == 3:
            return "gently used"
        elif rating == 4:
            return "pretty good"
        elif rating == 5:
            return "really great!"
