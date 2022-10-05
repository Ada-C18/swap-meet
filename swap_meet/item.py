class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
# Wave 3       
    def __str__(self):
        return "Hello World!"

# Wave 5
    def condition_description(self):
        if self.condition == 0:
            return "I dont like zero"
        elif self.condition == 1:
            return "I dont like one either"
        elif self.condition == 2:
            return "Maybe I like two"
        elif self.condition == 3:
            return "Hmmmm.....probably three is nice"
        elif self.condition == 4:
            return "I like four"
        elif self.condition == 5:
            return "Five is a nice number"
        


    
        
