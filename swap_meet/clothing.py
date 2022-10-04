from swap_meet.item import Item

class Clothing:
    def __init__(self, condition=0, age=0):
        super().__int__(category='Clothing', condition=condition, age=age)#Inheritance importing category from Item
    
    def __str__(self):
        return "The finest clothing you could wear."