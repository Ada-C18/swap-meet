class Item:
    def __init__(self,category= ""):
        self.category = category
        
    def get_category(self):
        return self.category
    
    def __str__(self):
        return "Hello World!"

