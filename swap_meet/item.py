from unicodedata import category


class Item:
    
    def __init__(self, category= None):
        self.category = category

        if self.category is None:
            self.category = ""

    

