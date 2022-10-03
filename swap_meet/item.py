# class Item(category=""):
#     self.category = category

class Item:
    def __init__(self, category = ""):
        self.category = category

    def __str__(self, item):
        return f'{item}'