from swap_meet.item import Item

class Decor(Item):
    
    category = "Decor"
    
    def __init__(self, category=category):
        super().__init__(self)
        self.category = category

    # def __init__(self, category):
    #     self.category = category
    
    def __str__(self):
        return ("Something to decorate your space.")