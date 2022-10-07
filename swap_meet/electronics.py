from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, category = "Electronics", condition = 0,year_created = None):
        super().__init__(category,condition,year_created)

    
    def __str__(self):
        return "A gadget full of buttons and secrets."