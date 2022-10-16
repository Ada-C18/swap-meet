from swap_meet.item import Item
class Decor(Item):
    """Expectation: Has an attribute category that is "Decor"
    Its stringify method returns "Something to decorate your space.
    All three classes and the Item class have an attribute called condition, which can be optionally provided in the initializer. The default value should be 0
    """
    
    def __init__(self,condition = 0):
        super().__init__(category = "Decor", condition = condition)

    ##Second solution to apply to other child classes
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
