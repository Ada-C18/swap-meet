class Item:

    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):

        if self.condition == 0.0:
            return "Very Poor"
        elif self.condition <= 1.0:
            return "Poor"
        elif self.condition <= 2.0:
            return "Fair"
        elif self.condition <= 3.0:
            return "Good"
        elif self.condition <= 4.0:
            return "Like New"
        else:
            return "New"





