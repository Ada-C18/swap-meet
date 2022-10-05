#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = category if category is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self, condition):
        describers = ["You might want gloves for this one..",
        "It..", 
        "Average wear and tear",
        "This looks almost new!",
        "This is NEW!"
        ]

        for item in len(describers):
            if describers.index(item) == round(condition):
                return item