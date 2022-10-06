from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition)
        print(super().__str__())


    def __str__(self):

        return("The finest clothing you could wear.")
