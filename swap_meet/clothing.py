from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category, condition):
        self.category = "Clothing"
        self.condition =  super(Item, self).condition_description(self)
        
        

        
    
    def __str__(self):
        self.Clothing = "The finest clothing you could wear."
        return self.Clothing
