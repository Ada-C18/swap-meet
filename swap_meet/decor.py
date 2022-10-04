from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "", condition = 0, age = float('inf')):
        super().__init__(category, condition, age)
        self.category = "Decor"
    
    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        return super().condition_description()