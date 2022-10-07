# from swap_meet.vendor import Vendor

################################## Wave 2 ##################################
class Item:
    def __init__(self,category = "",condition = 0):
        """Expectation: each Item will have an attribute named category, which is an empty string by default
        When we initialize an instance of Item, we can optionally pass in a string with the keyword argument category """
        self.category = category
        self.condition = condition 
        

################################## Wave 3 ##################################
    def __str__(self):
        return ("Hello World!")


################################## Wave 5 ##################################


    def condition_description(self):
        if self.condition <=2:
            return f"Fair condition:{round(self.condition,1)}"
        elif self.condition <=3:
            return f"Good condition: {round(self.condition,1)}"
        elif self.condition <=4:
            return f"Great condition: {round(self.condition,1)}"
        else:
            return f"Excellent condition: {round(self.condition,1)}"
