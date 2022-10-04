class Item:
    def __init__(self, category=None):
        category = category if category is not None else ""
        self.category = category 
    def stringify_item(self, item):
        self.item = item
        return str(item)