class Item:

    def __init__(self, category = ""):
        """
        sets up the Item instance with an optional category attribute
        """
        self.category = category

    def __str__(self):
        return "Hello World!"