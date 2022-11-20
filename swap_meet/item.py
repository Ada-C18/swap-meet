class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        if 0 <= self.condition < 1: return "use for parts"
        if 1 <= self.condition < 2: return "heavily used"
        if 2 <= self.condition < 3: return "used"
        if 3 <= self.condition < 4: return "fine"
        if 4 <= self.condition < 5: return "good as new"
        if self.condition == 5: return "mint!"