#from swap_meet.vendor import Vendor
class Item:
    def __init__(self, category=""):
       self.category = category
    
    def __str__(self):
        self.str = "Hello World!"
        return self.str