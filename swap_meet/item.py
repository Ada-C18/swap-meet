class Item:
    def __init__(self, category="", condition=0.0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0: 
            return "Condition is unknown"
        elif 1 <= self.condition < 3:
            return "It needs a lot of love"
        elif self.condition == 3:
            return "It just needs a little love"
        elif self.condition == 4: 
            return  "Very good"
        elif self.condition == 5:
            return "Like New!"