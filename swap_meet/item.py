class Item:
# Wave 2
    def __init__(self, category = None):
        # category is the property of Item
        if category:
            self.category = category
        else:
            self.category = ""
 
 # Wave 3
    def __str__(self):        
        return "Hello World!"

