class Vendor:
    
    def __init__(self, inventory=None):
        """
        Set up a Vendor instance using an optional list of 
        inventory items. 
        """

        # set up default empty list for self.inventory
        # Conditional expression doc: 
        # https://docs.python.org/3/reference/expressions.html#conditional-expressions        
        # empty list evaluates to Falsy 
        self.inventory = inventory if inventory else []

    def add(self, item):
        """
        Add an item to self.inventory. Returns the item. 
        """

        self.inventory.append(item)
        return item 

    def remove(self, item):
        """
        Remove item from self.inventory. Returns the item if successful,
        returns False if item not found in self.inventory.
        """

        # Use try/except to catch error and return false if 
        # item is not in list. 
        try:
            self.inventory.remove(item)
            return item 
        except ValueError:
            return False 





    