from swap_meet.item import Item

class Electronics(Item):
    # might need Super() in __init__
    # override the __str__ method
    def __init__(self, condition = 0):
    
        super().__init__(condition, category = "Electronics")
    

    def __str__(self):
        return "A gadget full of buttons and secrets."
