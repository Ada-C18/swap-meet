from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0.0, age = 0, room = "n/a"):
        super().__init__("Decor", condition, age)
        self.room = room
    
    def __str__(self):
        return "Something to decorate your space."