class Item:

    # TODO: maybe we should reorder these arguments if category is 
    # set by default in child classes?
    def __init__(self, category = "", condition=0):
        """
        sets up the Item instance with an optional category attribute
        """
        
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        