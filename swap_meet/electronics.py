class Electronics:
    
    def __init__(self, category = "Electronics", condition = 0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self, condition = 0.0):
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