Condition_Description ={
            0 : "heavily used",
            1 : "well loved",
            2 : "medium used",
            3 : "almost new",
            4 : "Open box",
            5 : "mint"
        }
        
class Item():
    def __init__(self,category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World"

    def condition_description(self):
        
        for condition, description in Condition_Description.items():
            if self.condition == condition:
                return description




