# Wave 2
#=========================================
class Item:
    def __init__(self, category = ""):
        if category:
            self.category = category
        else:
            self.category = ""

# Wave 3
#=========================================   
    # write stringify method that returns "Hello World!"
    def __str__(self):
        return "Hello World!"
        