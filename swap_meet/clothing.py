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
    def condition_description(self, bad, good, better, best, great):
        bad.condition = "bad"
        good.condition = "good"
        better.condition = "better"
        best.condition = "best"
        great.condition = "great"
    # needs to equal a number can think tomorrow 
        
