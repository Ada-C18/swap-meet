<<<<<<< HEAD
from swap_meet.item import Item
=======
from swap_meet.item import Item 
>>>>>>> d69aaf471ce85245128a1e61f5165aa3ece1a30c
class Decor:
    def __init__(self, category=None, condition=0):
        self.category = "Decor"
        self.condition = condition
        #super().__init__(category , condition)

    def __str__(self):
        return "Something to decorate your space."
