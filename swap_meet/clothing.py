from .item import Item
# from swap_meet.item import Item


# class Clothing:
class Clothing(Item):
    def __init__(self, condition=0.0):  # parameters  given by user
        super().__init__("Clothing", condition)
        # attributes

    def __str__(self):
        super().__str__()
        return "The finest clothing you could wear."
