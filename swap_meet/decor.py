from swap_meet.item import Item
class Decor(Item):
    def __init__(self,condition = 0):
        super().__init__(category = "Decor", condition = condition)

    ##Second solution
# class Decor(Item):
#     def __init__(self,condition = 0):
#         super().__init__(category ="",condition = 0):
#         self.category = "Decor"    

    ##Third solution
# class Decor(Item):
#     def __init__(self,condition = 0):
#         super().__init__("Decor",condition = 0):

    ##Fourth Solution

# class Decor(Item):
#     def __init__(self, condition = 0):
#         self.category = “Decor”
#         self.condition = condition
#Call super() for methods only

    
    def __str__(self):
        return "Something to decorate your space."
