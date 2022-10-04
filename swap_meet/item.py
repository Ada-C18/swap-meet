class Item():
    def __init__(self,category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World"

    def condition_description(self):
        if self.condition == 0 :
            return "heavily used"
        elif self.condition == 1:
            return "well loved"
        elif self.condition == 2:
            return "medium used"
        elif self.condition == 3:
            return "almost new"
        elif self.condition == 4:
            return "Open box"
        elif self.condition == 5:
            return "mint"






