class Item:

    def __init__(self, condition=0, category=""):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        conditions = {
            0: "not sellable",
            1: "heavily used",
            2: "decent condition",
            3: "slightly used",
            4: "like new",
            5: "mint condition",
        }
        return conditions[int(self.condition)]
