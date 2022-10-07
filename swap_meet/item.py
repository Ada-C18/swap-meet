class Item:
    def __init__(self, category=None, condition=0):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition
# stringifies class Item
    def __str__(self):
        return "Hello World!"
# creates descriptions of conditions
    def condition_description(self):
        if self.condition == 0:
            return "Horrible Condition >:("
        elif self.condition == 1:
            return "Heavily Used :("
        elif self.condition == 2:
            return "So-So condition :/"
        elif self.condition == 3:
            return "Decent :|"
        elif self.condition == 4:
            return "Gently Used :)"
        elif self.condition == 5:
            return "Like New! >:)"
        
# example: book = Item("book", "literature", 5)

