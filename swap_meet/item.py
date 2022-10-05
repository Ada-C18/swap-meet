class Item:
    def __init__(self,category = None, condition = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_rank(self):
        if self.condition == 1.0:
            return "Poor"
        elif self.contion == 2.0:
            return "Acceptable"
        elif self.contion == 3.0:
            return "Good"
        elif self.contion == 4.0:
            return "Very Good"
        elif self.contion == 5.0:
            return "Brand New"
        