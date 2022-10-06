class Item():
    def __init__(self, category=None, condition= None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return f"not worth it at all"
        elif self.condition <= 2: 
            return f"i'd think twice before purchasing"
        elif self.condition <= 3:
            return f"this is a bargain"
        elif self.condition <= 4: 
            return f"almost perfect"
        else:
            return f"perfect, perfect, perfect"
        


