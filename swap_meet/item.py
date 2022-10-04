class Item:
    def __init__(self, category=None):
        category = category if category is not None else ""
        self.category = category
    def __str__(self):
        return f"Hello World!"
