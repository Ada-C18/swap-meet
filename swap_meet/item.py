class Item:
    def __init__(self, category="", condition=0): #attribute named category which is an empty string
        self.category=category
        self.condition=condition
    
    def __str__(self): #stringify an instance of Item str() returns "Hello World!"
        return "Hello World!"

    def condition_description(self):
        
        if self.condition > 0 and self.condition < 1: 
            return "Ripped"
        elif self.condition ==1:
            return "Stained"
        elif self.condition==2:
            return "Heavily used"
        elif self.condition ==3:
            return "Medium used"
        elif self.condition ==4:
            return "Mint"
        elif self.condition ==5:
            return "New"
        else:
            return "Recicle"