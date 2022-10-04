class Item:

# Wave 2 & 5
    def __init__(self, category = None, condition = 0.0):  
        # category & condition are the property of Item     
        if category is None:
            category = ""
        self.category = category 
        self.condition = condition 


 # Wave 3
    def __str__(self):        
        return "Hello World!"


# Wave 5
    def condition_description(self, condition = 0.0):
        '''
        Describe the condition in words based on the value.
        '''
        if self.condition <= 1:
            return "Uhhh"
        elif self.condition <= 2 and self.condition >= 1:
            return "Bad Enough"
        elif self.condition <= 3 and self.condition >= 2:
            return "So so"
        elif self.condition <= 4 and self.condition >= 5:
            return "Nice Enough"
        elif self.condition <= 5:
            return "Sparkling"

