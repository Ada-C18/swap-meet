from swap_meet.item import Item
class Decor(Item):
    """
    A class to represent the category of the item.
    """
    
    def __init__(self, condition = ""):
        super().__init__("Decor", condition)
       
    def __str__(self):
        return "Something to decorate your space."