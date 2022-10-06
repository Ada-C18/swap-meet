class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition_description_list = ["Throw Away!",
        "Poor Condition",
        "Acceptable Condition",
        "Good Condition",
        "Very Good Condition",
        "New Condition"]
        return condition_description_list[int(self.condition) - 1]
    
    # What if condition was out of range (ex. condition = 7 or -1; 
    # write a test to raise index error or value error?)
