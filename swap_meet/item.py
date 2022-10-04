from swap_meet.vendor import Vendor

class Item:
    def __init__(self):
        self.category = ""

    def get_by_category(self, category_name):
        list_item = []
        for item in list(Item):
            if category_name == self.category:
                list_item.append(item)
                return list_item