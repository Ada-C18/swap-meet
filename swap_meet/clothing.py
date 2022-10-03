from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."
    
    # def condition_description(self):
    #     if self.condition == 5:
    #         return "Absolutely perfect! I love that for you (^‿◕)"
    #     elif self.condition > 4:
    #         return "Almost absolutely perfect! Aren't you lucky ☘☘☘"
    #     elif self.condition > 3:
    #         return "Not too shabby!"
    #     elif self.condition > 2:
    #         return "They're a little fixer upper"
    #     elif self.condition > 1:
    #         return "Be gentle with this one, it's a bit (or very) used"
    #     else:
    #         return "Do an exorcism first...just in case"