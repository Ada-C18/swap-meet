from swap_meet.item import Item

class Electronics:
    def __init__(self, category="Electronics", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return Item.__str__(self.category)

    def condition_description(self):
        return Item.condition_description(self.condition)