from swap_meet.item import Item
class Decor(Item):
    def __init__(self):
        super().__init__("Decor")
        # self.category = category


    def __str__(self):
        return f"Something to decorate your space."

    def condition_description(self):
        return ""