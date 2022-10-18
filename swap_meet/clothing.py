from swap_meet.item import Item
class Clothing (Item):
    def __init__(self, category="Clothing", condition=0, age=0):
        '''
        takes in a category string, with a default value "Clothing", 
        a condition float, and age to create an instance of Clothing
        '''
        super().__init__(category, condition, age)
        # self.category = "Clothing"
    
    def __str__(self):
        '''will return a description for clothing'''
        return "The finest clothing you could wear."
    
