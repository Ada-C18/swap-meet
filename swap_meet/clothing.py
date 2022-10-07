from hashlib import new


class Clothing:
    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "The finest clothing you could wear."

    def condition_description(self, poor=0, fair=1, good=2, excellent=3, perfect=4, new=5):
        self.poor = poor
        self.fair = fair
        self.good = good
        self.excellent = excellent
        self.perfect = perfect
        self.new = new