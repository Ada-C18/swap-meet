
class Vendor:
     # inventory (list of items)
    # accept item class instances

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item) #explore other removal methods
            return item
    
    def get_by_category(self, category):
        items_list = []
        for element in self.inventory:
            if element.category == category:
                items_list.append(element)

        return items_list
