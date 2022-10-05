from unicodedata import category


class Item:
    def __init__(self, category = None):
        self.category = category if category != None else ""


    
    def __str__(self):
        return f"Hello World!"