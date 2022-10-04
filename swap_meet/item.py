class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        dict_condition_description = {
            1: "Poor",
            2: "Heavily used",
            3: "Gently Used",
            4: "Like New",
            5: "New",
        }
        if self.condition:
            return f"{dict_condition_description[self.condition]}"