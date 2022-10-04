class Item:
    def __init__(self, category=""):
        self.category = category

    # __str__ is called when str() function is invoked on an object
    def __str__(self):
        return "Hello World!"
