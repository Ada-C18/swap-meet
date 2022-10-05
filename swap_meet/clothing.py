from .item import Item

class Clothing(Item):

    # category-specific constructor using "Clothing" as the 
    # default. 
    def __init__(self, category="Clothing", condition=0):

        # pass variables to the super().__init__ function
        # including the default category. 
        super().__init__(category, condition)

    def __str__(self):
        return "The finest clothing you could wear."
