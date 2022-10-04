class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category

    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        return f""