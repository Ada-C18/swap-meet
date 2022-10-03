# import swap_meet.item
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item) #is .remove the real thing to use?
        
        return item

    def get_by_category(self, a_category):
        self.a_category: a_category
        items = []
        for item in self.inventory:
            if item.category == a_category:
                items.append(item)
        return items