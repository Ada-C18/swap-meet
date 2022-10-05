from unicodedata import name


class Item:
    # each item will have attribute- empty list by default
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition

    # make a string method that always return Hello World!
    def __str__(self):
        return "Hello World!"

    # return a condition description based on condition
    def condition_description(self):

        condition_statements = {
            0: "mint condition",
            1: "new",
            2: "like new",
            3: "gently used",
            4: "signs of wear & tear",
            5: "heavily used"
        }

        for i in range(6):
            if self.condition == i:
                return condition_statements[i]
