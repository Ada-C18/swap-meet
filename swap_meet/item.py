class Item:
    
    def __init__(self, category=""):
        self.category = category
    
    # # pythonic convention: this method calls str() for custom objects to return 
    # # human-friendly (i.e., readible) output
    def __str__(self):
        return "Hello World!"