class Item:

    def __init__(self, category = "",condition = 0.0):
        self.category = category
        self.condition = condition
   
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 3.0:
            return"its pretty good"
        else:
            return "ehhhh nah"

    