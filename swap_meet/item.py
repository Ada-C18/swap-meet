class Item:
    def __init__(self, category="", condition=0.0, age=0):
        '''takes in a category string, condition float, and age integer to create an instance of Item'''
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        '''returns a description of the item condition'''
        # condition = {
        #     0:"Condition is unknown", 
        #     1: "It needs lots of love",
        #     2: "It needs some love",
        #     3: "It just needs a little love",
        #     4: "Very good",
        #     5: "Like New!"
        #     }
        # return condition[self.condition]
        if self.condition == 0: 
            return "Condition is unknown"
        elif 1 <= self.condition < 3:
            return "It needs a lot of love"
        elif 3 <= self.condition < 4:
            return "It just needs a little love"
        elif 4<= self.condition < 5: 
            return  "Very good"
        elif self.condition == 5:
            return "Like New!"