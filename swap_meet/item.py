

class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self):   #when you see a print statement that is on an object of class item, call this method!
        return f"Hello World!"
