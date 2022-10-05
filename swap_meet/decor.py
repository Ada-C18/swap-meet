from .item import Item

# class Decor(Item):
#     def __init__(self, category="Decor", condition=0):
#         self.category = category
#         self.condition = condition

# DISCUSS WITH GALINA - inheriting from Item and then overriding category?
# class Decor(Item):
#     def __init__(self, category="Decor", condition=0):
#         Item.__init__(self, category, condition)
#         self.category = category

# DISCUSS WITH GALINA - why can I not just inherit condition? When you call a superclass you can leave off "self"
class Decor(Item):
    def __init__(self, condition=0):
        super().__init__(category="Decor", condition=condition)
       
    
    def __str__(self):
        return "Something to decorate your space."