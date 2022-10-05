class Item:
    # get_by_category Wave 2 
    # Wave 3 stringify "Hello World!" with __str__
    def __init__(self, category=""):
        self.category = category
        # self.condition = condition

    def __str__(self):
        return "Hello World!"

    def get_by_category(self, category=""):
        self.category = category
            


