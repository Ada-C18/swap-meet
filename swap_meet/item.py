
class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):  
        return f"Hello World!"
    
    def condition_description(self):
        if self.condition >= 0 and self.condition < 1:
            return "You should reconsider getting this item"
        elif self.condition >= 1 and self.condition < 2:
            return "it's super old!"
        elif self.condition >= 2 and self.condition < 3:
            return "it's had a lifetime!"
        elif self.condition >= 3 and self.condition < 4:
            return "not too bad!"
        elif self.condition >= 4 and self.condition <= 5:
            return "Get it!" 
