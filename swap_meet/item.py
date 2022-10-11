class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "Are you sure this is second-hand?"
        elif 3 <= self.condition < 5:
            return "Pretty minty, if you ask me"
        elif 1.5 <= self.condition < 3:
            return "Probably best to clean this one first...."
        elif self.condition < 1.5:
            return "Are you sure you want this?"