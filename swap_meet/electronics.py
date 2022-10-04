class Electronics:
    def __init__(self, category ="Electronics", condition = 0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return f"A gadget full of buttons and secrets."

    def condition_description(self):
        return f"{self.condition}"
