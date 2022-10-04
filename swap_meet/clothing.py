'''
module: clothing.py
    class: Clothing
        attribute: .category
        method: __str__
'''

from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0, category = "Clothing"):
        super().__init__(category, condition)
        self.condition = condition

    def __str__(self): 
        return "The finest clothing you could wear."
