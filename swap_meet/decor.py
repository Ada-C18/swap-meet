from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=0):
        super().__init__(condition=condition)
        self.category = "Decor"
        

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        item_condition = super().condition_description()

        return item_condition
