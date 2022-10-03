class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self, condition):
        if condition == 1:
            return "Trash"
        elif condition == 2:
            return "Desperate"
        elif condition == 3:
            return "Alright"
        elif condition == 4:
            return "Good"
        else:
            return "Like New"

            