class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "This item is brand new!"
        elif self.condition >= 4:
            return "This item is slightly worn, but still in good shape."
        elif self.condition >= 3:
            return "This item is clearly secondhand, but not too bad."
        elif self.condition >= 2:
            return "This item needs cleaning, but might still be OK."
        elif self.condition >= 1:
            return "This item is in pretty bad shape."
        else:
            return "This item is so old and worn, it's almost unrecognizable."
