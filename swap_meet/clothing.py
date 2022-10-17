from swap_meet.item import Item

class Clothing(Item):
    '''Creating child class of item for clothing category.'''
    def __init__(self, condition=0, age=0):
        super().__init__("Clothing", condition, age)

    def __str__(self):
        return "The finest clothing you could wear."


