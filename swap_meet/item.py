class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(category):
        if category == "Clothing":
            return "The finest clothing you could wear."
        elif category == "Decor":
            return "Something to decorate your space."
        elif category == "Electronics":
            return "A gadget full of buttons and secrets."
        else:
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