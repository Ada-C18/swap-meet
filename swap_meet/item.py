class Item:
    def __init__(self, category=None):
        category = category if category is not None else ""
        self.category = category
    
    # if str(self):
    #     return "Hello World!"
    
    # def stringified_item(self, item):
    #     try: 
    #         self.item = item
    #         return str(item)
    #     except AssertionError:
    #         return "Hello World!"