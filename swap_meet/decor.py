class Decor:
    
    def __init__(self, category, condition=0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."