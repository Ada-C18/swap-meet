'''
module: item.py
    class: Item
        attribute: .inventory
        method: __str__ .condition_description
'''

class Item:

    def __init__(self, category = None, condition = 0):
        if category: # not empty:
            self.category = category
        else: 
            self.category = "" # default

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 5:
            return "Same as new!"
        elif self.condition >= 3 and self.condition < 5:
            return("Fair")
        elif self.condition >= 1 and self.condition < 3 :
            return("Not bad")
        elif self.condition < 1:
            return("You can throw away")
        else:
            return("don't know condition")
