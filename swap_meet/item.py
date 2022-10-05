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

        # switched the order of the statements to match the requirements
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
