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
