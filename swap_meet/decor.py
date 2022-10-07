from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=0, age=0):
        category = 'Decor'
        super().__init__(category = category, condition=condition, age=age)


    def __str__(self):
        return "Something to decorate your space."