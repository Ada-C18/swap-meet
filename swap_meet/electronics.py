from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, age=None, category="Electronics", condition=0):
        """
        Input: requires age, sets default category as "Electronics" 
        and optionally takes in condition as a parameter.
        Result: defines attributes category and condition
        """
        self.age = age
        self.category = category
        self.condition = condition

    def __str__(self):
        """
        When stringifying an instance using str(), returns
        "A gadget full of buttons and secrets."
        """
        return "A gadget full of buttons and secrets."