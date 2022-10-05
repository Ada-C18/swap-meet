
class Item:
    def __init__(self, category = "", condition = 0, age = 0):
       self.category = category
       self.condition = condition
       self.age = age
    def __str__(self):
        self.str = "Hello World!"
        return self.str

    def condition_description(self):
        if self.condition == 0:
            return "This is a no no, unless you want gross stuff."
        elif self.condition == 1:
            return "Meh, I still wouldn't go for it, unless it's scrap material."
        elif self.condition == 2:
            return "This is approaching okay"
        elif self.condition == 3:
            return "This is fine."
        elif self.condition == 4:
            return "This is nice, there's just light water damage."
        else:
            return "This is perfect."