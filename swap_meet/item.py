class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        descriptions = {
                        0: "Trash",
                        1: "Almost Trash", 
                        2: "Desperate",
                        3: "Alright", 
                        4: "Good", 
                        5: "Like New"
                        }
        return descriptions[self.condition]