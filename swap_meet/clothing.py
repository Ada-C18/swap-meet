
from swap_meet.item import Item


class Clothing:
    def __init__(self, condition = 0):
        self.category = condition


    def __str__(self):
        return "The finest clothing you could wear."
