class Item:
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return "Hello World!"

    