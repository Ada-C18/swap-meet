from swap_meet.item import Item


class Clothing(Item):

    def __init__(self,category = "Clothing", condition = 0,year_created = None):
        super().__init__(category,condition,year_created)

    
    def __str__(self):
        return "The finest clothing you could wear."
