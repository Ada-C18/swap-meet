class Item:
    def __init__(self, category=None, condition=None):
        category = category if category is not None else ""
        self.category = category
        condition = condition if condition is not None else 0.0
    def __str__(self):
        return f"Hello World!"
    def condition_description(self):
        if 0 <= self.condition < 1: 
            return f"Mint!"
        elif 1 <= self.condition < 2:
            return f"New!"
        elif 2 <= self.condition < 3:
            return f"Good!"
        elif 3 <= self.condition < 4:
            return f"Used!"
        elif 4 <= self.condition <= 5:
            return f"Heavily used!"




