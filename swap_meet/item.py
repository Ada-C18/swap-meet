class Item:

    def __init__(self, category="", condition=0,):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        conditions = {
            0: "horrible",
            1: "heavily used",
            2: "OK",
            3: "slightly used",
            4: "like new",
            5: "mint",
        }
        return conditions[int(self.condition)]