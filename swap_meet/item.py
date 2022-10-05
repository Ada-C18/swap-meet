import numbers


class Item:
    def __init__(self, condition = 0, category = ""):
        self.condition = condition if condition is not None else 0
        self.category = category if category is not None else ""
    
    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        condition_list = ["heavily used", "moderately used", "slightly used", "used", "almost new", "brand new"]
        
        for i in range(len(condition_list)):
            if i == self.condition:
                return condition_list[i]

        
        
        
        
# matched condition with index

#self.condtion get us a numbers
