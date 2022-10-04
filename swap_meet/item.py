class Item:
    '''add doc string'''
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        if self.category:
            return self.category
        else:
            return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Print 0"
        elif self.condition == 1:
            return "Print 1"
        elif self.condition == 2:
            return "Print 2"
        elif self.condition == 3:
            return "Print 3"
        elif self.condition == 4:
            return "Print 4"
        elif self.condition == 5:
            return "Print 5"
        else:
            return None





# '''All three classes and the `Item` class have an instance method named 
# `condition_description`, which should describe the condition in words based 
# on the value, assuming they all range from 0 to 5. These can be basic 
# descriptions (eg. 'mint', 'heavily used') but feel free to have fun with 
# these (e.g. 'You probably want a glove for this one..."). The one requirement 
# is that the `condition_description` for all three classes above have the same behavior.'''