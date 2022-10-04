class Item:
    
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = condition

    # def __str__(self) -> str:
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if int(self.condition) == 5:
            return "It's like it's never been used"
        elif int(self.condition) == 4:
            return "Great condition"
        elif int(self.condition) == 3:
            return "It looks well loved"
        elif int(self.condition) == 2:
            return "At least its free"
        elif int(self.condition) == 1:
            return "How is this still holding together?"
        elif int(self.condition) == 0:
            return "Firestarter"
