from swap_meet.item import Item

class Electronics(Item):
    """Inherits from 'Item' class and creates an 'Electronics' object."""
    
    def __init__(self, category= "Electronics", **kwargs):
    #https://stackoverflow.com/questions/66761435/child-class-override-parents-parameters
        super().__init__(**kwargs)
        self.category = category
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    

