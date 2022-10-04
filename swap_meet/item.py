from attr import validate

class Item:
    def __init__(self, category = None):
        #  category is an empty string
        if category is None:
            category = ""
        self.category = category       

    def __str__(self):
        return "Hello World!"
        
        

    
    
    
        
        