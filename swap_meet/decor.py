from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category="Decor", condition=0.0, age=0): 
        '''
        takes in a category string, with a default value "Decor", 
        a condition float, and age to create an instance of Decor
        ''' 
        super().__init__(category, condition, age)
        # self.category = "Decor"

    def __str__(self):
        '''will return a description for decor'''
        return "Something to decorate your space."
    