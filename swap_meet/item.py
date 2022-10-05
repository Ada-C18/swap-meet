# from msilib.schema import Condition

class Item:
    def __init__(self,category= "", condition =0.0, conditional_desc=""):
        self.category = category
        self.condition = condition
        self.conditional_desc = conditional_desc
        
    def get_category(self):
        return self.category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        return str(self.condition)
    
        # if self.condition == 0.0:
        #     self.coditional_desc = "bad"
        #     return self.coditional_desc
        # elif self.condition <= 1.0:
        #     self.conditional_desc = "poor"
        #     return self.coditional_desc
        # elif self.condition <= 2.0:
        #     self.conditional_desc = "acceptable"
        #     return self.coditional_desc
        # elif self.condition <= 3.0:
        #     self.conditional_desc = "fair"
        #     return self.coditional_desc
        # elif self.condition <= 4.0:
        #     self.conditional_desc = "good"
        #     return self.coditional_desc
        # elif self.condition <= 5.0:
        #     self.conditional_desc ="excellent"
        #     return self.coditional_desc
    

