from swap_meet.item import Item

# Wave 5
#=========================================  
class Electronics(Item):
    def __init__(self, condition=0):
        super().__init__(category = "Electronics", condition = condition)     

    def __str__(self):
        return "A gadget full of buttons and secrets."
