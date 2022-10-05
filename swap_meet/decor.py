from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = 0.0, conditional_desc=""):
        self.category = category
        self.condition = condition
        self.conditional_desc = conditional_desc
    
    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        return str(self.condition)