class Item:
    # each item will have attribute- empty list by default
    def __init__(self, category= None):
        self.category = category if category is not None else ""
    
    # stringify Item 
    def __str__(self)


