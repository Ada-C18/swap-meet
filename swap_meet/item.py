class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(condition):
        if condition < 1:
            return "Someone's trash is another's treasure."
        elif 1 <= condition < 2:
            return "Probably better to upcycle this!"
        elif 2 <= condition < 3:
            return "It needs some work to make it nice!"
        elif 3 <= condition < 4:
            return "Might have been sitting in storage for a while, but you wouldn't really know..."
        elif 4 <= condition <= 5:
            return "Looks like you bought it new yourself!"