from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, age=None, category="Clothing", condition=0):
        """
        Input: requires age, sets default category as "Clothing" 
        and optionally takes in condition as a parameter.
        Result: defines attributes category and condition
        """
        self.age = age
        self.category = category
        self.condition = condition

    def __str__(self):
        """
        When stringifying an instance using str(), returns
        "The finest clothing you could wear."
        """
        return "The finest clothing you could wear."