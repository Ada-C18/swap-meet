from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, category="Electronics", condition=0.0, age=0):
        '''
        takes in a category string, with a default value "Electronics", 
        a condition float, and age to create an instance of Electronics
        '''
        super().__init__(category, condition, age)
        # self.category = "Electronics"
    
    def __str__(self):
        '''will return a description of Electronics'''
        return "A gadget full of buttons and secrets."

