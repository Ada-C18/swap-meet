class Item:

    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition 
        self.age = age
        

    def __str__(self):
        return "Hello World!" 

    def condition_description(self):
        if self.condition == 0:
            return "mint"
        elif self.condition <= 1.0:
            return "brand new"
        elif self.condition <= 2.0:
            return "almost new"
        elif self.condition <= 3.0:
            return "used"
        elif self.condition <= 4.0:
            return "heavily used"
        elif self.condition <= 5.0:
            return "You probably want a glove for this one..."
        
        # return str(self.condition)
            

    
 
            