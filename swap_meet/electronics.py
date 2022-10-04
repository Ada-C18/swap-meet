from swap_meet.item import Item

class Electronics:
    def __init__(self, condition=0, age=0):
        super().__int__(category='Electronics', condition=condition, age=age)#Inheritance importing category from Item
    def __str__(self):
        return "A gaget full of buttons and secrets."
