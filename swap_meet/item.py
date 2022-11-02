class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 

    def get_by_category(self):
        pass
   
    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Unusable"
        elif self.condition == 1:
            return "Severely worn"
        elif self.condition == 2:
            return "Just a small hole"
        elif self.condition == 3:
            return "A few scratches"
        elif self.condition == 4:
            return "One light scratch"
        elif self.condition == 5:
            return "Best condition ever"