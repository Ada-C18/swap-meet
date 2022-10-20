class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_list = ["As Is", "Acceptable", "Good", "Very Good", "Like New", "New"]
        for i in range(len(condition_list)):
            if i == self.condition:
                return condition_list[i]








