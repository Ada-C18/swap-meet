class Item:

    def __init__(self, category=None, condition=None, age=None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
        self.age = age if age is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        conditions = {
            0: "Poor condition. Best for repurposing.",
            1: "Okay condition. Shows significant signs of use.",
            2: "Good condition. Shows normal signs of use.",
            3: "Great condition. Shows minor signs of use.",
            4: "Excellent condition. No signs of use.",
            5: "Brand new, never used."
        }

        return conditions[self.condition]
