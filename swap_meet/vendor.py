class Vendor:
    """creates a vendor object with an attribute called "inventory" and 2 methods: 
    "add" that adds items to the inventory, and 
    "remove" that removes item from the inventory."""
    def __init__(self, inventory = []):
        self.inventory = inventory
        
    def add(self, item):
        """adds given item to the inventory. Returns the item that was added."""
        if isinstance(item, list):
            self.inventory.extend(item)
        else:
            self.inventory.append(item)
        return item
    
    def remove(self, item):
        """removes given item from the inventory. Returns the item that was removed.
        If the inventory doesn't contain that item, returns False"""
        try: 
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
    

    

    


    