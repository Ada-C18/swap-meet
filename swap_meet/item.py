class Item:
    def __init__(self, category = ""):
        self.category = category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self,condition = 0):
        self.condition = condition 
        if condition == 0:
            condition_0_statement = "New with tags"
        if condition == 1:
            condition_1_statement = "New never been worn"
        if condition == 2:
            condition_2_statement = "First come first served"
        if condition == 3:
            condition_3_statement = "Heavily used"
        if condition == 4:
            condition_4_statement = "Garbage bag condition"
        if condition == 5:
            condition_5_statement = "Hazmat suit neeeded"
        
