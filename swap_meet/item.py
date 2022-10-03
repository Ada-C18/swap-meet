class Item:
    def __init__(self,category=""):
        self.category=category
    
    def __str__(self):
        print(self.category)
        return "Hello World!"
