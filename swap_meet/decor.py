from swap_meet.item import Item

class Decor(Item):
    def __init__(self, age=None, category="Decor", condition=0):
        """
        Input: requires age, sets default category as "Decor" 
        and optionally takes in condition as a parameter.
        Result: defines attributes category and condition
        """
        self.age = age
        self.category = category
        self.condition = condition

    def __str__(self):
        """
        When stringifying an instance using str(), returns
        "Something to decorate your space."
        """
        return "Something to decorate your space."