class Item:
    def __init__(self, category="",  condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1:
            return "Gross"
        elif self.condition <= 2:
            return "Wear and Tear"
        elif self.condition <= 3:
            return "Not great"
        elif self.condition <= 4:
            return "Gently used"
        else:
            return "Like new"
