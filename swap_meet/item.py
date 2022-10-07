
class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "YIKES..."
        elif self.condition >= 1 and self.condition < 2:
            return "Not the worst but DEFINITELY not the best"
        elif self.condition >= 2 and self.condition < 3:
            return "Has seen better days"
        elif self.condition >= 3 and self.condition < 4:
            return "Average"
        elif self.condition >= 4 and self.condition < 5:
            return "Like new"
        elif self.condition == 5:
            return "PERFECT!"
