class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Probably best for scraps"
        elif self.condition == 1:
            return "Pretty heavily used"
        elif self.condition == 2:
            return "Moderate wear"
        elif self.condition == 3:
            return "Lightly used"
        elif self.condition == 4:
            return "Like new self.condition"
        elif self.condition == 5:
            return "Brand new in box/ with tags"