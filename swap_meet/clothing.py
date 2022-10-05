class Clothing:
    def __init__(self,category = "Clothing"):
        self.category = category if category is not None else ""
    def __init__(self, category=None, condition=0.0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."


    # "Aviva try git push"
    # "clothing..how hard can it be"
    def condition_description(self):
        # self.condition_dict = condition_dict
        condition_dict= {"worst": 0, "bad": 1, "good":2, "better":3, "best":4, "great":5}

        
        for key, value in condition_dict:
            if self.condition == condition_dict.values():
                return condition_dict.keys()

        # if self.condition == 0:
        #     return "worst"
        # elif self.condition == 1:
        #     return "bad"
        # elif self.condition == 2:
        #     return "good"
        # elif self.condition == 3:
        #     return "better"
        # elif self.condition == 4:
        #     return "best"
        # elif self.condition == 5:
        #     return "great"
        
    



        
