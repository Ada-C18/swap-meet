from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0, age = float('inf')):
        super().__init__("Electronics", condition, age)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    def condition_description(self):
        return super().condition_description()
