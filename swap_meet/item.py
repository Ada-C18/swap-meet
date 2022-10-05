class Item:
    def __init__(self, category = "",condition = 0 ):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        five_condition_description = "New with tags"
        four_condition_description = "Never been worn"
        three_condition_description = "Used"
        two_condition_description = " Heavily used"
        one_condition_description = "Hazmat suit needed"
        
        if self.condition == 5:
            condition_description = five_condition_description
        if self.condition == 4:
            condition_description = four_condition_description
        if self.condition == 3:
            condition_description = three_condition_description
        if self.condition == 2:
            condition_description = two_condition_description
        if self.condition == 1:
            condition_description = one_condition_description
        
        return condition_description
        
