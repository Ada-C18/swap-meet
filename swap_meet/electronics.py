from swap_meet.item import Item

class Electronics:
    def __init__(self, category=None, condition=0.0):
        self.category = "Electronics"
        self.condition = condition
        #super().__init__(category , condition)



    def __str__(self):
        return "A gadget full of buttons and secrets."
