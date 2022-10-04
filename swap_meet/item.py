class Item:
    def __init__(self, category="", condition=0):
        if category is None:
            self.category = ""
        self.category = category
        self.condition = condition

    def __str__(self_):
       return "Hello World!"
