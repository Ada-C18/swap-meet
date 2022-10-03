from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category=None):
        self.category = category if category is not None else ""

    def get_by_category(self):
        for item in self.inventory:
            list_of_cat = []
            list_of_cat.append(item.category)
            return list_of_cat
