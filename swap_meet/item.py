class Item:
    
    def __init__(self, category = "", condition = None):
        self.category = category
        if condition is None:
            condition = 0
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Revive me from the dead"
        elif self.condition == 1:
            return "I could use some love"
        elif self.condition == 2:
            return "Not too shabby, eh?"
        elif self.condition == 3:
            return "Great deal over here"
        elif self.condition == 4:
            return "I sparkle"
        elif self.condition == 5:
            return "I sparkle even in the darkle"