from swap_meet.item import Item

class Clothing(Item):
    """
    A class to represent the category of the item.
    """

    def __init__(self, condition = 0):
        super().__init__("Clothing", condition)
            
    def __str__(self):
        return "The finest clothing you could wear."

    
   