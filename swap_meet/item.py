#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self, condition):
        describers = ["You might want gloves for this one..",
        "It..", 
        "Average wear and tear",
        "This looks almost new!",
        "This is NEW!"
        ]
       # if float(condition):
        #    condition = round(condition)

        for item in len(describers):
            if describers.index(item) == condition:
                return item