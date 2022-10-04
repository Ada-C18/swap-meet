

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    
    # stringify item to print hello world
    def __str__(self):
        return "Hello World!"
    
    """
    instance method on parent class
    """
    def condition_description(self):
        if self.condition < 1:
            return "Schwag"
        elif self.condition < 2:
            return "Hard Pass"
        elif self.condition < 3:
            return "Fair"
        elif self.condition < 4:
            return "Dank"
        else:
            return "Primo"
