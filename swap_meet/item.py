class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        return f"{self.condition}"
