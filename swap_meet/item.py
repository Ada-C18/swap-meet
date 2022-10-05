class Item:
    def __init__(self, condition=0, category=None):
        self.condition = condition
        if not category:
            self.category = ""
        else: 
            self.category = category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 5:
            return "New"
        elif 3 <= self.condition < 5:
            return "Fine"
        else:
            return "Poor"
