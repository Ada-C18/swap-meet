from swap_meet.item import Item

class Decor(Item):
    """Inherits from 'Item' class and creates a 'Decor' object."""
    
    def __init__(self, category= "Decor", **kwargs):
    #https://stackoverflow.com/questions/66761435/child-class-override-parents-parameters
        super().__init__(**kwargs)
        self.category = category
    
    def __str__(self):
        return "Something to decorate your space."
    
