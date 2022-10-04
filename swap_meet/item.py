class Item:
    def __init__(self, category=None, condition=None):
        if not category:
            self.category = ""
        else:
            self.category = category

        if not condition:
                self.condition = 0.0
        else:
            self.condition = condition

    def __str__(self):
        return("Hello World!")

    def condition_description(self):
        if self.condition <= 1:
            return f"Terrible condition"
        elif self.condition <= 2:
            return f"Bad condition"
        elif self.condition <=3:
            return f"Meh condition"
        elif self.condition <=4:
            return f"Decent condition"
        else:
            return f"Great condition"
