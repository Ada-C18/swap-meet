

class Item:
    def __init__(self,category ="",condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return(f"Superb")
        elif self.condition == 4:
            return(f"Good")
        elif self.condition == 3:
            return(f"OK")
        elif self.condition == 2 :
            return(f"Not too bad")
        elif self.condition == 1:
            return(f"OH MY GOD")
        elif self.condition == 0:
            return (f"Ahhh")