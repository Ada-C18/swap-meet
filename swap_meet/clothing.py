from swap_meet.item import Item

class Clothing:
    def __init__(self,category = "Clothing", condition = '0'):
        super().__init__(condition="0")
        self.category = category

    def __str__(self):
        return "The finest clothing you could wear."