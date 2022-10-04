from unicodedata import category

class Item:
    
    def __init__(self, category= None, condition=0):
        self.category = category
        self.condition = condition

        if self.category is None:
            self.category = ""

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return (f'Proceed with caution')
        elif self.condition == 1:
            return (f'Yikes...')
        elif self.condition == 2:
            return (f'You sure about this?')
        elif self.condition == 3:
            return (f"Doesn't look too bad")
        elif self.condition == 4:
            return (f"looks like new")
        elif self.condition == 5:
            return (f"You're coming home with me")