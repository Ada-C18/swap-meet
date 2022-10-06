from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        list_by_category = []

        # I don't know what else to call it... so it's thing for now =/
        for thing in self.inventory:
            if thing.category == category:
                list_by_category.append(thing)
        return list_by_category

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        other_vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        best_item_list = self.get_by_category(category)
        if not best_item_list:
            return None
    
        best_item = max(best_item_list, key=lambda item: item.condition)
        return best_item 

    def swap_best_by_category(self, other, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True

        