from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,category="Electronics",condition=0) -> None:
        self.category=category
        self.condition=condition
    
    def __str__(self): 
        return "A gadget full of buttons and secrets."
        
    #def condition_decription(self):
        #return "cloth"
        