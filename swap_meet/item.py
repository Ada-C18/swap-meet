class Item:
    def __init__(self, category = None):
        if category == None:
            category = ""
        self.category = category
        