from swap_meet.item import Item

class Decor:
    def __init__(self, condition=0, age=0):
        super().__int__(category='Decor', condition=condition, age=age)#Inheritance importing category from Item
    def __str__(self):
        return "Something to decorate your space."