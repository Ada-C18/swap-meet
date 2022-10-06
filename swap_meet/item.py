class Item:
    def __init__(self, category = None, condition = None, age = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
        self.age = age if age is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "0 flaws: the best you're going to get"
        if 1 >= self.condition > 0:
            return "1 flaw: you're never going to financially recover from this"
        if 2 >= self.condition > 1:
            return "2 flaws: you might have buyer's remorse"
        if 3 >= self.condition > 2:
            return "3 flaws: in between gently used and roughly used"
        if 4 >= self.condition > 3:
            return "4 flaws: you're going to need a LOT of glue"
        if 5 >= self.condition > 4:
            return "5 flaws: gift it to someone you 'love'"