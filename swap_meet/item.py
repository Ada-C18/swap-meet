class Item:
    def __init__(self, category=None, condition=0.0):
        self.category = category if category is not None else ""
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_dict = {"worst": 0, "bad": 1,
                          "good": 2, "better": 3, "best": 4, "great": 5}
        for key, value in condition_dict.items():
            if self.condition == value:
                return key
