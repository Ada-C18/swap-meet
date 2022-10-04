

class Item:
    def __init__(self, category = ""):
        self.category = category

    """""
    stringify item to print hello world

    """""
    def __str__(self):
        return "Hello World!"