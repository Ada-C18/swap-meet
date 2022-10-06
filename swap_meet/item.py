class Item:
    def __init__(self, category = None, condition = None, age = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
        self.age = age if age is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_descriptions = [
            "0 flaws: the best you're going to get", 
            "1 flaw: you're never going to financially recover from this",
            "2 flaws: you might have buyer's remorse",
            "3 flaws: in between gently used and roughly used",
            "4 flaws: you're going to need a LOT of glue",
            "5 flaws: gift it to someone you 'love'"
            ]
        return condition_descriptions[int(self.condition)]