class Vendor:
    # init attributes: inventory(list)
    def __init__(self, inventory =  []):
        self.inventory = inventory



    # method to add items to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
        


    # method to remove items from inventory
    def remove(self, item):
        try:
            self.inventory.remove(item)
        except(ValueError):
            return False

        return item
    # iterates through inventory and puts into seperate list based on category attribute
    def get_by_category(self, category):
        filter = []
        for item in self.inventory:
            if item.category == category:
                filter.append(item)

        return filter 
