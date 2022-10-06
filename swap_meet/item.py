class Item:
    def __init__(self, category="", condition=0):
        if category is None:
            self.category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
       return "Hello World!"

    def condition_description(self):
        # changed from if-elif to dictionary
        '''Returns descriptions of condition based on condition value.'''
        condition_dict = {
            0:"Yo this is trash.",
            1:"Definitely used. Perhaps too much.",
            2:"If you're okay with some dings and things.",
            3:"Lots of life left if you handle with care.",
            4:"Barely even a scratch.",
            5:"ULTRA RARE PIECE, NWOT CONDITION.",

        }
        if self.condition in condition_dict:
            return condition_dict[self.condition]
            
       