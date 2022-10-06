from swap_meet.item import Item
class Decor(Item):
    def __init__(self,condition = 0):
        super().__init__(category = "Decor", condition = condition)

    ##Second solution
# class Decor(Item):
#     def __init__(self,condition = 0):
#         super().__init__("Decor",condition)

    ##Third Solution - we not use super() for attributes. Call super() for methods only
# class Decor(Item):
#     def __init__(self, condition = 0):
#         self.category = “Decor”
#         self.condition = condition
    
    def __str__(self):
        return "Something to decorate your space."
