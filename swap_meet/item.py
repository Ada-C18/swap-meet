class Item:
    def __init__(self, age=None, condition=None, category=None):
        self.age = age if age is not None else 0
        self.condition = condition if condition is not None else 0.0
        category = category if category is not None else ""
        self.category = category
    def __str__(self):
        return f"Hello World!"
    def condition_description(self):
        if 0 <= self.condition < 1: 
            return f"Heavily used"
        elif 1 <= self.condition < 2:
            return f"Used!"
        elif 2 <= self.condition < 3:
            return f"Good!"
        elif 3 <= self.condition < 4:
            return f"New!"
        elif 4 <= self.condition <= 5:
            return f"Mint!"




