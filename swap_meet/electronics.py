from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition=0.0, conditional_desc="" ):
        self.category = category
        self.condition = condition
        self.conditional_desc = conditional_desc
        
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    def condition_description(self):
        return str(self.condition)

