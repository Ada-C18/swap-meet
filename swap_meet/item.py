class Item:
    def __init__(self, category="", condition: float=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        zero = f"Not even good enough to recycle."
        one = f"Unusable, but you might still want it."
        two = f"Has some life left."
        three = f"Appropriately mediocre."
        four = f"Works well for what it is."
        five = f"Amaaaazing!"
        
        condition_list = [one, two, three, four, five]
        
        # we're using round to make sure any float values
        # are rounded up or down to their nearest integer
        # we know the rounded number will be an integer
        # because we've not passed in an argument for ndigits

        return condition_list[round(self.condition)-1]