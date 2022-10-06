from swap_meet.item import Item

# Wave 5
#=========================================  
class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."  