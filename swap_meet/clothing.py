from swap_meet.item import Item

class Clothing(Item):
    """Inherits from 'Item' class and creates a 'Clothing' object."""
    
    def __init__(self, category= "Clothing", **kwargs):
    #https://stackoverflow.com/questions/66761435/child-class-override-parents-parameters
        super().__init__(**kwargs)
        self.category = category
    
    def __str__(self):
        return "The finest clothing you could wear."
    
