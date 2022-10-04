class Vendor:
    
    def __init__(self, inventory = []):
        # if self.inventory is None:
        #     self.inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            if not item in self.inventory:
                return False
            self.inventory.remove(item)
            return item
        except SyntaxError as err:
            print("Please enter a valid item")