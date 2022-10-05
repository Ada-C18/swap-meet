class Item:
    def __init__(self, category = ""):
        self.category = category
        # if condition == None:
        #     self.condition = 0
        # else:
        # self.condition = condition
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "This is probably out of your price range normally"
        elif self.condition >= 4:
            return "This is still pretty good, just not mint."
        elif self.condition >= 3:
            return "This isn't bad, could be better."
        elif self.condition >= 2:
            return "Not the best, you could live without it."
        elif self.condition > 0:
            return "Put this down and walk away."
