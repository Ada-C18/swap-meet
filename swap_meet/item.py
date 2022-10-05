class Item:
    def __init__(self, category = None, condition = 0.0):
        self.category = category if category is not None else ""
        self.condition = condition
    def __str__(self):
        return "Hello World!"