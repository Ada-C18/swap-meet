class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(category):
            return "Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "Someone's trash is another's treasure."
        elif 1 <= self.condition < 2:
            return "Probably better to upcycle this!"
        elif 2 <= self.condition < 3:
            return "It needs some work to make it nice!"
        elif 3 <= self.condition < 4:
            return "Might have been sitting in storage for a while, but you wouldn't really know..."
        elif 4 <= self.condition <= 5:
            return "Looks like you bought it new yourself!"