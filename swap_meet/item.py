class Item:
    '''
    All three classes and the Item class have an attribute called condition,
    which can be optionally provided in the initializer. The default value 
    should be 0.
    '''
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Ew. You don't want that."
        elif self.condition == 1:
            return "Maybe you need gloves for that."
        elif self.condition == 2:
            return "Heavily Used"
        elif self.condition == 3:
            return "Decent"
        elif self.condition == 4:
            return "Lightly Used"
        elif self.condition == 5:
            return "Like new!"
