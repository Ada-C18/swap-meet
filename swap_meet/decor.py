class Decor:
    def __init__(self, category ="Decor", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return f"Something to decorate your space."

    def condition_description(self):
        return f"{self.condition}"