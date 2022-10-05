from swap_meet.item import Item

class Decor(Item):

    def __init__(self, category = "Decor", condition = 0,year_created = None):
        super().__init__(category,condition,year_created)


    
    def __str__(self):
        return "Something to decorate your space."