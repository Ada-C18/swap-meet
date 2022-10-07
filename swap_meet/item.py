class Item:
    # get_by_category Wave 2 
    # Wave 3 stringify "Hello World!" with __str__
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def get_by_category(self, category=""):
        self.category = category

    def condition_description(self):
        condition_names = {
            0: "Awful condition",
            1: "Pretty bad condition",
            2: "Decent condition",
            3: "Pretty good condition",
            4: "Good condition",
            5: "Perfect condition"
        }
        
        return condition_names[self.condition]
         


