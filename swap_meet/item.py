
class Item:
    def __init__(self, category=''):
        self.category = category

        if self.category == "":
            return None
    
        else:
            return category
 

# item_a = Item(category="clothing")
# item_b = Item(category="electronics")
# item_c = Item(category="clothing")