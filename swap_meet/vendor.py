class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category=""):
        list_of_items_by_category = []
        for item in self.inventory:
            if item.category == category:
                list_of_items_by_category.append(item)
        return list_of_items_by_category
    
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or \
            not their_item in friend_vendor.inventory:
            return False
        item_to_give = self.remove(my_item)
        friend_vendor.add(item_to_give)
        item_to_get = friend_vendor.remove(their_item)
        self.add(item_to_get)
        return True
