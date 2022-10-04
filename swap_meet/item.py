


class Item():
    #class Item has __init__ and __str__
    def __init__(self, category = "", condition=0):
        self.category = category
        self.condition = condition


    def __str__(self) -> str:
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "mint"
        elif self.condition == 1:
            return "open box"
        elif self.condition == 2:
            return "almost new"
        elif self.condition == 3:
            return "midum use"
        elif self.condition == 4:
            return "Well loved"
        elif self.condition == 5:
            return "heavely used"



    
