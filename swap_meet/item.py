class Item:
    def __init__(self, category="", condition: float=0, age: int=100):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        zero = f"Not even good enough to recycle."
        one = f"Unusable, but you might still want it."
        two = f"Has some life left."
        three = f"Appropriately mediocre."
        four = f"Works well for what it is."
        five = f"Amaaaazing!"
        
        condition_list = [zero, one, two, three, four, five]
        
        # we're using round to make sure any float values
        # are rounded up or down to their nearest integer
        # we know the rounded number will be an integer
        # because we've not passed in an argument for ndigits

        # we didn't use floor division because we didn't want to force
        # a condition that was very close to the upward condition down
        # a slot when picking a condition description =>
        # e.g., if Item.condition = 3.9, condition_description should return
        # description four and not description three.

        return condition_list[round(self.condition)]