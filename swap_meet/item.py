#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        describers = ["You might want gloves for this one..",
        "It could look worse", 
        "Average wear and tear",
        "This looks almost new!",
        "This is NEW!"
        ]
        counter = 0
        while counter < len(describers):

            for item in range(len(describers) + 1):
                if item == self.condition:
                    return describers[item - 1]
                counter += 1