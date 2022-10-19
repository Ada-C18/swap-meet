from swap_meet.item import Item

class Electronics(Item):
    
    category = "Electronics"
    def __init__(self, category=category):
        super().__init__(self)
        self.category = category

    # def __init__(self, category):
    #     self.category = category
    
    def __str__(self):
        return ("A gadget full of buttons and secrets.")
