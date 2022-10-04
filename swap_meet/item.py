class Item:

    def __init__(self, category=""):
        self.category = category

    def __str__(self, string="Hello World!"):
        return string
    
    def condition_description(self, condition):
        descriptions = {
                        1: "Trash", 
                        2: "Desperate",
                        3: "Alright", 
                        4: "Good", 
                        5: "Like New"
                        }
        return descriptions[condition] if condition in descriptions.keys() else "Other"
            