# from swap_meet.vendor import Vendor

class Item:
    def __init__(self,category = "",condition = 0):
        self.category = category
        self.condition = condition 
        
    # def __init__(self, category = None, condition = 0):
    #     if category:
    #         self.category = category
    #     else:
    #         self.category = ""
    
    
    
    def __str__(self):
        return ("Hello World!")
    
    def condition_description(self):
        if self.condition <=2:
            return f"Fair condition:{round(self.condition,1)}"
        elif self.condition <=3:
            return f"Good condition: {round(self.condition,1)}"
        elif self.condition <=4:
            return f"Great: {round(self.condition,1)}"
        else:
            return f"Excellent condition: {round(self.condition,1)}"
