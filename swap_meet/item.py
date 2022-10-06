class Item:
    def __init__(self,category=None,condition=0,age=0):
        self.condition=condition
        self.age=age
        if category == None:
            self.category = ""
        else:
            self.category = category    
    
    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):
        if self.condition == 0:
            return "0"
        elif self.condition > 0 and self.condition <= 1:
            return "0-1"
        elif self.condition > 1 and self.condition <= 2:
            return "1-2"
        elif self.condition > 2 and self.condition <= 3:
            return "2-3"
        elif self.condition > 3 and self.condition <= 4:
            return "3-4"
        elif self.condition > 4 and self.condition < 5:
            return "4-5"
        elif self.condition == 5:
            return "5"   
