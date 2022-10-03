class Item:
    def __init__(self, category = None):
        self.category = category if category is not None else ""
    # def get_by_category(self, items):
    #     self.category = items
    #     return items