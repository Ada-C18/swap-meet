class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Horrible"
        elif 0 < self.condition <= 1:
            return "Used"
        elif 1 < self.condition <= 2:
            return "Lightly Used"
        elif 2 < self.condition <= 3:
            return "Good"
        elif 3 < self.condition <= 4:
            return "Very Good"
        elif 4 < self.condition <= 5:
            return "Excellent"
            