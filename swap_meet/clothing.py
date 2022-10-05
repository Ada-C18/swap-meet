# from swap_meet.item import Item
class Clothing:
    def __init__(self,category = "Clothing"):
        self.category = category if category is not None else ""
    def __init__(self, category=None, condition=0.0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        condition_dict= {"worst": 0, "bad": 1, "good":2, "better":3, "best":4, "great":5}

        for key, value in condition_dict.items():
            if self.condition == value:
                return key

        
    



        
