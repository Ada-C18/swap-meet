class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 

    def get_by_category(self):
        pass
   
    def __str__(self):
        return f"Hello World!"

    def condition_description(self, condition):
        for clothes in range(0, 6):
            if condition == 0:
                return "Unusable"
            elif condition == 1:
                return "Severely worn"
            elif condition == 2:
                return "Just a small hole"
            elif condition == 3:
                return "A few scratches"
            elif condition == 4:
                return "One light scratch"
            else:
                return "Best condition ever"