class Item:
    '''add doc string'''
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "This is pretty much garbage."
        elif self.condition <= 1:
            return "Not great."
        elif self.condition <= 2:
            return "This is ok."
        elif self.condition <= 3:
            return "Not too bad."
        elif self.condition <= 4:
            return "Looking good."
        elif self.condition <= 5:
            return "Perfect."

