from swap_meet.item import Item

class Vendor():
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    def get_by_category(self, category=""):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory) < 1 or len(other_vendor.inventory) < 1:
            return False
        else:
            first_item = self.inventory.pop(0)
            other_first_item = other_vendor.inventory.pop(0)
            self.remove(first_item)
            other_vendor.add(first_item)
            self.add(other_first_item)
            other_vendor.remove(other_first_item)
        return True

    def get_best_by_category(self, category):
        list_of_items = self.get_by_category(category)
        best_item = self.find_max_item(list_of_items) 
        return best_item  

    def find_max_item(self, items):
        if len(items) == 0:
            return None
        best_item = items[0] 
        for item in items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
            #swap my_best_item with their_best_item
            my_best_item = self.get_best_by_category(their_priority)
            their_best_item = other.get_best_by_category(my_priority)
            return self.swap_items(other, my_best_item, their_best_item)

    def get_best_by_category(self, category=""):

        if len(self.get_by_category(category)) == 0:
            return None
        best_item = (max(self.get_by_category(category), key=lambda x:x.condition))
        return best_item

        swap_items = self.swap_items(other, my_priority, their_priority)

        if swap_items == False:
            return False
        return True