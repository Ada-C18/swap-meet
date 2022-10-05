from swap_meet.item import Item

class Clothing(Item):
    def __init__(self,category ="Clothing", condition=0.0, conditional_desc=" "):
        # super().__init__(category= "", condition =0.0, conditional_desc="")
        self.category = category
        self.condition = condition
        self.conditional_desc = conditional_desc
        
    def __str__(self):
        return "The finest clothing you could wear."
    
    def condition_description(self):
        return str(self.condition)