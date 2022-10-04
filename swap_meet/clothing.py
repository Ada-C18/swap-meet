class Clothing:
    
    def __init__(self, category ="Clothing", condition = 0):
        self.category = category

    def __str__(self):
        return f"The finest clothing you could wear."

    def condition_description(self):
        pass