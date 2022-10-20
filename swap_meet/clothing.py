from swap_meet.item import Item

class Clothing(Item):
    
    # category = "Clothing"
    
    def __init__(self, category = "Clothing"):
        super().__init__(self, condition = 0)
        self.category = category

        
        

    # def __init__(self, category):
    #     self.category = category
    
    def __str__(self):
        return ("The finest clothing you could wear.")