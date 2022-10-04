# from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Worn"
        elif self.condition == 1:
            return "No good"
        elif self.condition == 2:
            return "Not bad"
        elif self.condition == 3:
            return "Average"
        elif self.condition == 4:
            return "Very good"
        elif self.condition == 5:
            return "Excellent"
        else:
            Raise Exception("Condition is not right!")
        