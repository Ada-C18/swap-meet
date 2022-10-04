class Item:
    '''add doc string'''
    def __init__(self, category=""):
        self.category = category
    
    def __str__(self):
        if self.category:
            return self.category
        else:
            return "Hello World!"


