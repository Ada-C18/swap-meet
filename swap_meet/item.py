class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        description = ""
        if self.condition == 0: 
            description = "Unsellable"
        elif 0 < self.condition <= 2:
            description = "Very Used"
        elif 2 < self.condition <= 4:
            description = "Okay"
        elif 4 < self.condition <=5:
            description = "Just like new"
        return description         

            