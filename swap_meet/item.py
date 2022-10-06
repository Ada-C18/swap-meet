from unicodedata import name


class Item:
    def __init__(self, category=None, condition=0):
        # set category if it is provided, or set to empty string
        self.category = category if category is not None else ""
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        condition_statements = {
            0: "heavily used",
            1: "signs of wear & tear",
            2: "gently used",
            3: "like new",
            4: "new",
            5: "mint condition"
        }

        for i in range(6):
            if self.condition == i:
                return condition_statements[i]
