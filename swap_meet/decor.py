'''
module: decor.py
    class: Decor
        attribute: .category
        method: __str__
'''

from .item import Item

class Decor(Item):
    def __init__(self, condition = 0, category = "Decor"):
        super().__init__(category, condition)
        self.condition = condition

    def __str__(self): 
        return "Something to decorate your space."
