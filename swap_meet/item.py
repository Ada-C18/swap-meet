import numbers


class Item:
    def __init__(self, condition = 0, category = ""):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        condition_list = ["heavily used", "moderately used", "slightly used", "used", "almost new", "brand new"]
        
        for i in range(len(condition_list)):
            print(i)
            if i == self.condition:
                return condition_list[i]

        
        
        
        
# matched condition with index

#self.condtion get us a numbers
