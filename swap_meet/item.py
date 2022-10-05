class Item:
    def __init__(self, category="", condition: float=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        one = f"This is a one"
        two = f"This is a two"
        three = f"This is a three"
        four = f"This is a four"
        five = f"This is a five"
        
        condition_list = [one, two, three, four, five]
        
        return condition_list[self.condition-1]