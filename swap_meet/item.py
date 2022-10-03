class Item:
    # each item will have attribute- empty list by default
    def __init__(self, category= None):
        self.category = category if category is not None else ""
    
    # takes one argument (string => category) and returns list of items
    # in the inventory with that category


